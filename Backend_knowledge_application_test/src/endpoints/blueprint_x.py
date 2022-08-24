from flask import Blueprint, jsonify, request
#from ..api_spec import
from ..app import db
from ..models import User


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
          parameters:
            required:  true
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
        
    user = User.add_user(_full_name=name, _email=email, _password_hash=password)

    return jsonify(user.json())

@blueprint_x.route('/read/<user_id>', methods=['GET'])
def user_read(user_id):
    
    """Gist detail view.
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
              schema: ReadSchema
          
      tags:
      - User Management
   """
    #data = request.get_json()

    employee = User.query.get(int(user_id))
    
    if employee:
        return jsonify(employee.json())
        
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
