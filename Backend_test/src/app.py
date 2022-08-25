from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
login_manager = LoginManager()
# login_manager.session_protection = "strong"
# login_manager.login_view = "/api/docs/#/User%20Management/post_api_v1_user_management_login"
# login_manager.login_message_category = "info"

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint for auth routes in our app
    from .endpoints.blueprint_x import blueprint_x
    from .endpoints.swagger import swagger_ui_blueprint, SWAGGER_URL
    from .api_spec import spec

    # register blueprints. ensure that all paths are versioned!
    app.register_blueprint(blueprint_x, url_prefix="/api/v1/user-management")
    # app.register_blueprint(blueprint_y, url_prefix="/api/v1/publication-management")
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    with app.test_request_context():
        # register all swagger documented functions here
        for fn_name in app.view_functions:
            if fn_name == 'static':
                continue
            print(f"Loading swagger docs for function: {fn_name}")
            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)

    @app.route("/api/swagger.json")
    def create_swagger_spec():
        return jsonify(spec.to_dict())

    from .models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
