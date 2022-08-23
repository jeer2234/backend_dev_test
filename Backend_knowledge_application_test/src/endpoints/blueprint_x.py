from flask import Blueprint, jsonify, request
from ..models import User
from .. import db

# define the blueprint
blueprint_x = Blueprint(name="user-management", import_name=__name__)

# note: global variables can be accessed from view functions
x = 5


# add view function to the blueprint
@blueprint_x.route('/logout', methods=['GET'])
def user_logout():
    """
        ---
        get:
          description: logout endpoint
          responses:
            '200':
              description: call successful
              content:
                application/json:
                  schema: OutputSchema
          tags:
              - User Management
        """
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)


# add view function to the blueprint
@blueprint_x.route('/update', methods=['PUT'])
def user_update():
    """
        ---
        put:
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
              - User Management
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
    """
            ---
            post:
              description: login endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: UserLoginSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserSchema
              tags:
                  - User Management
            """

    # form = LoginForm()


@blueprint_x.route('/create', methods=['POST'])
def user_create():
    """
            ---
            post:
              description: login endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: UserLoginSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserSchema
              tags:
                  - User Management
            """
    data = request.get_json()

    # code to validate and add user to database goes here
    email = data['email']
    name = data['fullname']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        output = {'message': 'email already i use'}
        return jsonify(output)


@blueprint_x.route('/read', methods=['GET'])
def user_read():
    """
            ---
            get:
              description: logout endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: IdInputSchema

              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserSchema
              tags:
                  - User Management
            """
    data = request.get_json()

    employee = User.query.filter_by(id=data["user_id"]).first()
    if employee:
        return  # user profile schema object jsonfy
    return f"Employee with id ={data['user_id']} Doenst exist"


@blueprint_x.route('/delete', methods=['DELETE'])
def user_delete():
    """
                ---
                delete:
                  description: logout endpoint
                  requestBody:
                    required: true
                    content:
                        application/json:
                            schema: IdInputSchema

                  responses:
                    '200':
                      description: call successful
                      content:
                        application/json:
                          schema: UserSchema
                  tags:
                      - User Management
                """
