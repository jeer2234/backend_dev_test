from flask import Blueprint, jsonify, request
from .forms import LoginForm


# define the blueprint
blueprint_x = Blueprint(name="blueprint_x", import_name=__name__)

# note: global variables can be accessed from view functions
x = 5


# add view function to the blueprint
@blueprint_x.route('/test', methods=['GET'])
def test():
    """
        ---
        get:
          description: test endpoint
          responses:
            '200':
              description: call successful
              content:
                application/json:
                  schema: OutputSchema
          tags:
              - testing
        """
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)


# add view function to the blueprint
@blueprint_x.route('/plus', methods=['POST'])
def plus_x():
    """
        ---
        post:
          description: increments the input by x
          requestBody:
            required: true
            content:
                application/json:
                    schema: InputSchema
          responses:
            '200':
              description: call successful
              content:
                application/json:
                  schema: OutputSchema
          tags:
              - calculation
        """
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val + x
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)

@blueprint_x.route('/login', methods=['POST'])
def login():
    form = LoginForm()
