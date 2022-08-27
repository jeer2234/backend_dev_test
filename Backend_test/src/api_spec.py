"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields, validate

# Create an APISpec
spec = APISpec(
    title="My App",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


# User Management schemas

class IdInputSchema(Schema):
    id = fields.Int(description="An string number.", required=True)


class UserParameter(Schema):
    user_id = fields.Int()


class UserSchema(Schema):
    email = fields.Email(description="your email.", required=True)


class UserLoginSchema(UserSchema):
    password = fields.Str(description="your password.", validate=validate.Length(min=6), required=True)


class UserCreateSchema(UserLoginSchema):
    full_name = fields.Str()


class UserUpdateSchema(UserLoginSchema):
    full_name = fields.Str(load_default='')
    email = fields.Email(load_default='')
    password = fields.Str(load_default='')


class UserProfile(IdInputSchema, UserSchema):
    full_name = fields.Str()


class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)


# publication Management schemas


class PublicationUpdateSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    body = fields.Str()


class QuerySchema(Schema):
    priority = fields.Str(validate=validate.OneOf(["low", "high"]))
    status = fields.Bool(alidate=validate.OneOf([True, False]))


class UpdateOutputSchema(QuerySchema, PublicationUpdateSchema):
    pass


class PublicationDetailSchema(UpdateOutputSchema):
    user_id = fields.Int()
    created_at = fields.DateTime()
    published_at = fields.DateTime()
    updated_at = fields.DateTime()


# register  user management schemas with spec


spec.components.schema("IdInputSchema", schema=IdInputSchema)
spec.components.schema("OutputSchema", schema=OutputSchema)
spec.components.schema("UserParameter", schema=UserParameter)
spec.components.schema("UserLoginSchema", schema=UserLoginSchema)
spec.components.schema("UserCreateSchema", schema=UserCreateSchema)
spec.components.schema("UserProfile", schema=UserProfile)
spec.components.schema("UserUpdateSchema", schema=UserUpdateSchema)

# register  publication management schemas with spec

spec.components.schema("PublicationUpdateSchema", schema=PublicationUpdateSchema)
spec.components.schema("UpdateOutputSchema", schema=UpdateOutputSchema)
spec.components.schema("QuerySchema", schema=QuerySchema)

# add swagger tags that are used for endpoint annotation
tags = [
    {'name': 'Publication Management',
     'description': " user publication's management"
     },
    {'name': 'User Management',
     'description': 'User functionality endpoints.'
     },
]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)
