from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# init SQLAlchemy, LoginManager and Migrate, so we can use it later in our app
login_manager = LoginManager()
# login_manager.login_view = "/api/docs/#/User%20Management/post_api_v1_user_management_login"
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    username = "postgres"
    password = "jeer27541355"
    dbname = "backend_dev"

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.config['CSRF_ENABLED'] = True
    app.config['DEVELOPMENT'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    # blueprint for auth routes in our app
    from .endpoints.user_management import user_blueprint
    from .endpoints.publication_management import publication_blueprint
    from .endpoints.swagger import swagger_ui_blueprint, SWAGGER_URL
    from .api_spec import spec

    # register blueprints. ensure that all paths are versioned!
    app.register_blueprint(user_blueprint, url_prefix="/api/v1/user-management")
    app.register_blueprint(publication_blueprint, url_prefix="/api/v1/publication-management")
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
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
