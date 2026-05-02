import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from core.models import Recipe, Tag, Ingredient
from django.contrib.auth import get_user_model

def seed_data():
    User = get_user_model()
    # Ensure we have a user
    user, _ = User.objects.get_or_create(email='admin@example.com', defaults={'name': 'Admin User', 'password': 'password123'})
    
    # Delete old garbage recipes
    Recipe.objects.all().delete()
    Tag.objects.all().delete()
    Ingredient.objects.all().delete()
    
    # Create tags
    tag_italian, _ = Tag.objects.get_or_create(name='Italian', user=user)
    tag_healthy, _ = Tag.objects.get_or_create(name='Healthy', user=user)
    tag_spicy, _ = Tag.objects.get_or_create(name='Spicy', user=user)
    tag_dessert, _ = Tag.objects.get_or_create(name='Dessert', user=user)
    
    # Create ingredients
    ing_pasta, _ = Ingredient.objects.get_or_create(name='Pasta', user=user)
    ing_tomato, _ = Ingredient.objects.get_or_create(name='Tomato Sauce', user=user)
    ing_chicken, _ = Ingredient.objects.get_or_create(name='Chicken Breast', user=user)
    ing_chocolate, _ = Ingredient.objects.get_or_create(name='Dark Chocolate', user=user)
    
    # Create Recipes
    r1 = Recipe.objects.create(
        title='Classic Spaghetti Bolognese',
        time_minutes=45,
        price='12.99',
        description='A classic Italian pasta dish with rich meat sauce.',
        user=user
    )
    r1.tags.add(tag_italian)
    r1.ingredients.add(ing_pasta, ing_tomato)
    
    r2 = Recipe.objects.create(
        title='Grilled Chicken Salad',
        time_minutes=20,
        price='9.50',
        description='Healthy grilled chicken salad with vinaigrette dressing.',
        user=user
    )
    r2.tags.add(tag_healthy)
    r2.ingredients.add(ing_chicken)
    
    r3 = Recipe.objects.create(
        title='Spicy Arrabiata Pasta',
        time_minutes=30,
        price='11.00',
        description='Spicy tomato pasta with garlic and chili flakes.',
        user=user
    )
    r3.tags.add(tag_italian, tag_spicy)
    r3.ingredients.add(ing_pasta, ing_tomato)
    
    r4 = Recipe.objects.create(
        title='Decadent Chocolate Lava Cake',
        time_minutes=40,
        price='8.99',
        description='Rich chocolate dessert with a gooey center.',
        user=user
    )
    r4.tags.add(tag_dessert)
    r4.ingredients.add(ing_chocolate)
    
    print("Database seeded with 4 beautiful food recipes!")

if __name__ == '__main__':
    seed_data()
