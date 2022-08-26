from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user  # login_required
# from ..api_spec import
# from ..app import db
from ..models import User

# define the blueprint
user_blueprint = Blueprint(name="user-management", import_name=__name__)

# add view function to the blueprint
@user_blueprint.route('/logout', methods=['GET'])
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
@user_blueprint.route('/update', methods=['PUT'])
def user_update():
    """
            ---
            put:
              description: user update endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: UserUpdateSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UserCreateSchema
              tags:
                  - User Management
            """
    if current_user.is_authenticated:

        data = request.get_json()
        for test in list(data):
            if not data[test]:
                del data[test]

        current_user.update_user(**data)
        return jsonify(data)

    return jsonify({'error': "couldn't update user"})


@user_blueprint.route('/login', methods=['POST'])
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


@user_blueprint.route('/create', methods=['POST'])
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

    if user:
        output = {'message': 'email already i use'}
        return jsonify(output)

    user = User.add_user(_full_name=name, _email=email, _password_hash=password)

    return jsonify(user.json())


@user_blueprint.route('/read/<user_id>', methods=['GET'])
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

    user = User.query.get(int(user_id))

    if user:
        return jsonify(user.json())

    return jsonify({"error": "Employee id Doesnt exist"})


@user_blueprint.route('/delete', methods=['DELETE'])
def user_delete():
    """
                ---
                delete:
                  description: delete current user endpoint

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
        current_user.delete_user()
        # test to see if after being the user deleted you can use login required endpoints

        return jsonify({'msg': 'your user has been successfully deleted'})
    return jsonify({'error': 'you need to be login to delete your user'})
