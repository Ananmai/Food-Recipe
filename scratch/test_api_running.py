import urllib.request
import urllib.parse
import json

base_url = 'http://127.0.0.1:8080'

print("--- Testing Unauthenticated Access ---")
try:
    req = urllib.request.Request(f'{base_url}/api/recipe/recipes/')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Expected Error (Unauthorized): {e}")

print("\n--- Creating User ---")
user_data = json.dumps({
    'email': 'curluser@example.com',
    'password': 'password123',
    'name': 'Curl User'
}).encode('utf-8')
try:
    req = urllib.request.Request(f'{base_url}/api/user/create/', data=user_data, headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    print("User Created:", response.read().decode('utf-8'))
except Exception as e:
    print(f"Error Creating User: {e}")

print("\n--- Getting Token ---")
token_data = json.dumps({
    'email': 'curluser@example.com',
    'password': 'password123'
}).encode('utf-8')
try:
    req = urllib.request.Request(f'{base_url}/api/user/token/', data=token_data, headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    res_data = json.loads(response.read().decode('utf-8'))
    token = res_data.get('token')
    print("Token Retrieved:", token)
except Exception as e:
    print(f"Error Getting Token: {e}")

if 'token' in locals() and token:
    headers = {'Authorization': f'Token {token}', 'Content-Type': 'application/json'}
    
    print("\n--- Creating Recipe ---")
    recipe_data = json.dumps({
        'title': 'Curl Recipe',
        'time_minutes': 15,
        'price': '8.50',
        'description': 'Recipe created via script',
        'tags': [{'name': 'ScriptTag'}],
        'ingredients': [{'name': 'ScriptIngredient'}]
    }).encode('utf-8')
    try:
        req = urllib.request.Request(f'{base_url}/api/recipe/recipes/', data=recipe_data, headers=headers)
        response = urllib.request.urlopen(req)
        print("Recipe Created:", response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error Creating Recipe: {e}")

    print("\n--- Fetching Recipes (Paginated) ---")
    try:
        req = urllib.request.Request(f'{base_url}/api/recipe/recipes/', headers=headers)
        response = urllib.request.urlopen(req)
        print("Recipes List:", response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error Fetching Recipes: {e}")
