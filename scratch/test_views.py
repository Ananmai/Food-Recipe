import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from core.models import Recipe, Tag, Ingredient

User = get_user_model()
user1, _ = User.objects.get_or_create(email='user1@example.com', name='User 1')
user2, _ = User.objects.get_or_create(email='user2@example.com', name='User 2')

client1 = APIClient()
client1.force_authenticate(user=user1)

client2 = APIClient()
client2.force_authenticate(user=user2)

print("--- Testing Tag CRUD ---")
# Create
res = client1.post('/api/recipe/tags/', {'name': 'Vegan'})
print("Create Tag User 1:", res.status_code, res.data)
tag_id = res.data['id']

# List (Retrieve)
res = client1.get('/api/recipe/tags/')
print("List Tags User 1:", len(res.data['results']), res.data['results'])

# Test User isolation
res2 = client2.get('/api/recipe/tags/')
print("List Tags User 2:", len(res2.data['results']))

# Update
res = client1.patch(f'/api/recipe/tags/{tag_id}/', {'name': 'Vegetarian'})
print("Update Tag User 1:", res.status_code, res.data)

# Delete
res = client1.delete(f'/api/recipe/tags/{tag_id}/')
print("Delete Tag User 1:", res.status_code)


print("\n--- Testing Recipe CRUD ---")
res = client1.post('/api/recipe/recipes/', {
    'title': 'Test Recipe',
    'time_minutes': 10,
    'price': '5.00',
    'tags': [{'name': 'Breakfast'}]
}, format='json')
print("Create Recipe User 1:", res.status_code, res.data)
recipe_id = res.data['id']

res = client1.get('/api/recipe/recipes/')
print("List Recipes User 1:", len(res.data['results']), res.data['results'][0]['title'])

res = client1.delete(f'/api/recipe/recipes/{recipe_id}/')
print("Delete Recipe User 1:", res.status_code)
