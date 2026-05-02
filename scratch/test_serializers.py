import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from django.contrib.auth import get_user_model
from recipe.serializers import RecipeSerializer

User = get_user_model()
user, _ = User.objects.get_or_create(email='test_serializer@example.com', name='Serializer Tester')

class MockRequest:
    def __init__(self, user):
        self.user = user

request = MockRequest(user=user)

payload = {
    'title': 'Chocolate Cake',
    'time_minutes': 60,
    'price': '15.00',
    'description': 'A delicious chocolate cake.',
    'tags': [{'name': 'Dessert'}, {'name': 'Baking'}],
    'ingredients': [{'name': 'Cocoa Powder'}, {'name': 'Flour'}]
}

serializer = RecipeSerializer(data=payload, context={'request': request})
if serializer.is_valid():
    recipe = serializer.save(user=user)
    print("Recipe Created Successfully!")
    print("Title:", recipe.title)
    print("Tags:", [t.name for t in recipe.tags.all()])
    print("Ingredients:", [i.name for i in recipe.ingredients.all()])
else:
    print("Validation Error:", serializer.errors)

print("\n--- Testing Update ---")
update_payload = {
    'title': 'Vegan Chocolate Cake',
    'tags': [{'name': 'Dessert'}, {'name': 'Vegan'}],
    'ingredients': [{'name': 'Cocoa Powder'}, {'name': 'Almond Flour'}]
}

update_serializer = RecipeSerializer(instance=recipe, data=update_payload, partial=True, context={'request': request})
if update_serializer.is_valid():
    updated_recipe = update_serializer.save()
    print("Recipe Updated Successfully!")
    print("Title:", updated_recipe.title)
    print("Tags:", [t.name for t in updated_recipe.tags.all()])
    print("Ingredients:", [i.name for i in updated_recipe.ingredients.all()])
else:
    print("Validation Error:", update_serializer.errors)
