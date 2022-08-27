import os
import requests


def test_user_read(client):
    response = client.get('/api/v1/user-management/read/3')

    assert response.get_json() == {
        "email": "user@example.com",
        "full_name": "string",
        "id": 3}
