import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()
user1, _ = User.objects.get_or_create(email='filteruser@example.com', name='Filter User')

client = APIClient()
client.force_authenticate(user=user1)

print("--- Adding Data ---")
t1 = client.post('/api/recipe/tags/', {'name': 'Vegan'}).data['id']
t2 = client.post('/api/recipe/tags/', {'name': 'Dessert'}).data['id']
i1 = client.post('/api/recipe/ingredients/', {'name': 'Sugar'}).data['id']
i2 = client.post('/api/recipe/ingredients/', {'name': 'Salt'}).data['id']

client.post('/api/recipe/recipes/', {
    'title': 'Vegan Sugar Cookie',
    'time_minutes': 20,
    'price': '3.00',
    'tags': [{'name': 'Vegan'}, {'name': 'Dessert'}],
    'ingredients': [{'name': 'Sugar'}]
}, format='json')

client.post('/api/recipe/recipes/', {
    'title': 'Salty Snack',
    'time_minutes': 10,
    'price': '2.00',
    'tags': [],
    'ingredients': [{'name': 'Salt'}]
}, format='json')

print("\n--- Testing Search ---")
res = client.get('/api/recipe/recipes/?search=Vegan')
print("Search 'Vegan':", [r['title'] for r in res.data['results']])

print("\n--- Testing Filtering ---")
res = client.get(f'/api/recipe/recipes/?tags={t1}')
print(f"Filter by tag {t1} (Vegan):", [r['title'] for r in res.data['results']])

res = client.get(f'/api/recipe/recipes/?ingredients={i2}')
print(f"Filter by ingredient {i2} (Salt):", [r['title'] for r in res.data['results']])
