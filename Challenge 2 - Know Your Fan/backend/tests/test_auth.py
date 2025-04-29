import pytest
from app.models.user import User

def test_register(client):
    response = client.post('/auth/register', json={
        'full_name': 'New User',
        'email': 'new@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'

def test_register_existing_email(client, test_user):
    response = client.post('/auth/register', json={
        'full_name': 'Another User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert response.json['error'] == 'Email already registered'

def test_register_missing_fields(client):
    response = client.post('/auth/register', json={
        'full_name': 'New User',
        'email': 'new@example.com'
    })
    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'

def test_login(client, test_user):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json
    assert 'user' in response.json
    assert response.json['user']['email'] == 'test@example.com'

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json['error'] == 'Invalid email or password'

def test_login_missing_fields(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com'
    })
    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields' 