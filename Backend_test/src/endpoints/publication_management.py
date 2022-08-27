from flask import Blueprint, jsonify, request
from flask_login import current_user
# from ..api_spec import
# from ..app import db
from ..models import Publication, User

# define the blueprint
publication_blueprint = Blueprint(name="publication-management", import_name=__name__)


# add view function to the blueprint
@publication_blueprint.route('/update', methods=['PUT'])
def publication_update():
    """
            ---
            put:
              description: user update endpoint
              parameters:
                - in: query
                  schema: QuerySchema
              requestBody:
                required: true
                content:
                    application/json:
                        schema: PublicationUpdateSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: UpdateOutputSchema
              tags:
                  - Publication Management
            """
    if current_user.is_authenticated:
        pass

    data = request.get_json()

    for values in list(data):
        if not data[values]:
            del data[values]

    query = request.args.to_dict()

    for values in list(query):
        if not query[values]:
            del query[values]

    data.update(query)

    Publication.update_publication(**data)

    return jsonify(data)


@publication_blueprint.route('/create', methods=['POST'])
def publication_create():
    """
            ---
            post:
              description: create publication endpoint
              requestBody:
                required: true
                content:
                    application/json:
                        schema: PublicationUpdateSchema
              responses:
                '200':
                  description: call successful
                  content:
                    application/json:
                      schema: PublicationDetailSchema
              tags:
                  - Publication Management
            """
    if not current_user.is_authenticated:
        return jsonify({'msg': 'you need to be login to create a publication'})

    data = request.get_json()
    publication = Publication.add_publication(_title=data['title'], _description=data['description'],
                                              _body=data['body'],
                                              _author=current_user)

    return jsonify(publication.json())


@publication_blueprint.route('/read', methods=['GET'])
def publications_read():
    """
    ---
    get:
      content:
        application/json:


      responses:
        200:
          content:
            application/json:
              schema: UserProfile

      tags:
      - Publication Management
   """

    user = User.query.get()

    if user:
        return jsonify(user.json())

    return jsonify({"error": "Employee id Doesnt exist"})


@publication_blueprint.route('/read/<user_id>', methods=['GET'])
def publication_read(user_id):
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
      - Publication Management
   """

    user = User.query.get(int(user_id))

    if user:
        return jsonify(user.json())

    return jsonify({"error": "Employee id Doesnt exist"})


@publication_blueprint.route('/delete', methods=['DELETE'])
def publication_delete():
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
                      - Publication Management
                """

    if current_user.is_authenticated:
        current_user.delete_user()
        # test to see if after being the user deleted you can use login required endpoints

        return jsonify({'msg': 'your user has been successfully deleted'})
    return jsonify({'error': 'you need to be login to delete your user'})
