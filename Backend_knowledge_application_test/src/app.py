"""Flask Application"""

# load libaries
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import sys

# load modules
from .config import  Config
from .endpoints.blueprint_x import blueprint_x
# from .endpoints.blueprint_y import blueprint_y
from .endpoints.swagger import swagger_ui_blueprint, SWAGGER_URL
from .api_spec import spec


# init Flask app
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_x, url_prefix="/api/v1/path_for_blueprint_x")
# app.register_blueprint(blueprint_y, url_prefix="/api/v1/path_for_blueprint_y")
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
