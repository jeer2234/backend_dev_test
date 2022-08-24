"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="My App",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


# Define schemas


class UserSchema(Schema):
    fullname = fields.Str()
    email = fields.Email(description="your email.", required=True)


class UserLoginSchema(UserSchema):
    password = fields.Int(description="your password.", required=True)


class PublicationSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    priority = fields.Str()
    status = fields.Str()
    published_time = fields.TimeDelta()  # (seconds, minutes, hours, days, etc.),
    user = fields.Str()
    created_at = fields.TimeDelta()
    updated_at = fields.TimeDelta()


class IdInputSchema(Schema):
    number = fields.Int(description="An integer.", required=True)


class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)
    
class UserParameter(Schema):
    user_id = fields.Str()
    
class ReadSchema(UserParameter):
    content = fields.Str()


# register schemas with spec


spec.components.schema("Input", schema=IdInputSchema)
spec.components.schema("Output", schema=OutputSchema)
spec.components.schema("Login", schema=UserLoginSchema)
spec.components.schema("UserResponse", schema=UserSchema)
spec.components.schema("UserParameter", schema=UserParameter)
spec.components.schema("ReadSchema",schema=ReadSchema)


# add swagger tags that are used for endpoint annotation
tags = [
    {'name': 'Publication Management',
     'description': 'management of publications of users.'
     },
    {'name': 'User Management',
     'description': 'User functionality endpoints.'
     },
]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)
