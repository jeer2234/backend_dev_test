import os
import requests


def test_user_read(client):
    response = client.get('/api/v1/user-management/read/1')
    
    assert  response.get_json() == {
  "email": "jeer2234@gmail.com",
  "full_name": "javier espinoza",
  "id": 1 }