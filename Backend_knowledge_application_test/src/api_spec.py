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
    
class IDinputSchema(Schema):
    id = fields.Int(description="An string number.", required=True)
    
class UserParameter(Schema):
    user_id = fields.Int()
    
    
class UserSchema(Schema):
    email = fields.Email(description="your email.", required=True)
       
        
class UserLoginSchema(UserSchema):
    password = fields.Str(description="your password.", required=True);


class UserCreateSchema(UserLoginSchema):
    full_name = fields.Str()


class UserProfile(IDinputSchema, UserSchema):
    full_name = fields.Str()
    
    
class PublicationSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    priority = fields.Str()
    status = fields.Str()
    published_time = fields.TimeDelta()  # (seconds, minutes, hours, days, etc.),
    user = fields.Str()
    created_at = fields.TimeDelta()
    updated_at = fields.TimeDelta()
    
class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)



# register schemas with spec


spec.components.schema("IDinputSchema", schema=IDinputSchema)
spec.components.schema("OutputSchema", schema=OutputSchema)
spec.components.schema("UserParameter", schema=UserParameter)
spec.components.schema("UserLoginSchema", schema=UserLoginSchema)
spec.components.schema("UserCreateSchema", schema=UserCreateSchema)
spec.components.schema("UserProfile", schema=UserProfile)


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
