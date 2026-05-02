import urllib.request
import urllib.parse
import json

BASE_URL = 'http://127.0.0.1:8000/api/user/'

def make_request(endpoint, data=None, headers=None, method=None):
    url = BASE_URL + endpoint
    req_headers = {'Content-Type': 'application/json'}
    if headers:
        req_headers.update(headers)
    
    req_data = None
    if data:
        req_data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(url, data=req_data, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            return response.getcode(), json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())

print("1. Creating User...")
status, body = make_request('create/', data={
    'email': 'testuser2@example.com',
    'password': 'password123',
    'name': 'Test User 2'
})
print("Create User Response:", status, body)

print("\n2. Getting Token...")
status, body = make_request('token/', data={
    'email': 'testuser2@example.com',
    'password': 'password123'
})
print("Get Token Response:", status, body)
token = body.get('token')

print("\n3. Managing Profile...")
headers = {'Authorization': f'Token {token}'}
status, body = make_request('me/', headers=headers)
print("Get Profile Response:", status, body)

status, body = make_request('me/', headers=headers, data={'name': 'Updated Test User 2'}, method='PATCH')
print("Update Profile Response:", status, body)
