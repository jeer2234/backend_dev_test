from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
# from ..api_spec import
#from ..app import db
from ..models import User

# define the blueprint
blueprint_x = Blueprint(name="user-management", import_name=__name__)

# note: global variables can be accessed from view functions
x = 5


# add view function to the blueprint
@blueprint_x.route('/logout', methods=['GET'])
# @login_required
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
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'success': 'hello there'})

    return jsonify({'error': 'you need to be login to use this endpoint'})


# add view function to the blueprint
@blueprint_x.route('/update', methods=['PUT'])
def user_update():
    """
            ---
            put:
              description: user update endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: UserParameter
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserParameter
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
                      schema: UserProfile
              tags:
                  - User Management
            """
    if current_user.is_authenticated:
        return jsonify(current_user.json())

    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if user is None or not user.check_password(data["password"]):
        return jsonify({'error': 'Invalid username or password'})

    login_user(user, remember=True)
    return jsonify(user.json())


@blueprint_x.route('/create', methods=['POST'])
def user_create():
    """
            ---
            post:
              description: create endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: UserCreateSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserProfile
              tags:
                  - User Management
            """
    data = request.get_json()

    # code to validate and add user to database goes here
    email = data['email']
    name = data['full_name']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        output = {'message': 'email already i use'}
        return jsonify(output)

    user = User.add_user(_full_name=name, _email=email, _password_hash=password)

    return jsonify(user.json())


@blueprint_x.route('/read/<user_id>', methods=['GET'])
def user_read(user_id):
    """
    ---
    get:
      content:
        application/json:
      parameters:
        - in: path
          schema: UserParameter


      responses:
        200:
          content:
            application/json:
              schema: UserProfile
          
      tags:
      - User Management
   """
    # data = request.get_json()

    user = User.query.get(int(user_id))

    if user:
        return jsonify(user.json())

    return jsonify({"error": "Employee id Doesnt exist"})


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
