import pytest
from app.models.fan import Fan

def test_get_fans(client, test_fan):
    response = client.get('/fans/')
    assert response.status_code == 401  # Unauthorized without token
    
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    # Get fans with token
    response = client.get('/fans/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['email'] == 'fan@example.com'

def test_get_fan(client, test_fan):
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    response = client.get(f'/fans/{test_fan.id}', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['email'] == 'fan@example.com'

def test_create_fan(client):
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    response = client.post('/fans/', 
        json={
            'name': 'New Fan',
            'email': 'newfan@example.com',
            'location': 'New Location'
        },
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 201
    assert response.json['email'] == 'newfan@example.com'

def test_create_fan_existing_email(client, test_fan):
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    response = client.post('/fans/', 
        json={
            'name': 'Another Fan',
            'email': 'fan@example.com',
            'location': 'Another Location'
        },
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 400
    assert response.json['error'] == 'Email already registered'

def test_update_fan(client, test_fan):
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    response = client.put(f'/fans/{test_fan.id}', 
        json={
            'name': 'Updated Fan',
            'location': 'Updated Location'
        },
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Fan'
    assert response.json['location'] == 'Updated Location'

def test_delete_fan(client, test_fan):
    # Login to get token
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = login_response.json['token']
    
    response = client.delete(f'/fans/{test_fan.id}', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['message'] == 'Fan deleted successfully' 