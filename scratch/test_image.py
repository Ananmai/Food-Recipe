import os
import sys
import django
from io import BytesIO
from PIL import Image

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from core.models import Recipe

User = get_user_model()
user1, _ = User.objects.get_or_create(email='imageuser@example.com', name='Image User')

recipe = Recipe.objects.create(
    user=user1,
    title='Image Recipe',
    time_minutes=10,
    price='5.00'
)

client = APIClient()
client.force_authenticate(user=user1)

print("--- Testing Image Upload ---")

# Create a dummy image
image = Image.new('RGB', (100, 100), color=(255, 0, 0))
img_io = BytesIO()
image.save(img_io, format='JPEG')
img_io.seek(0)
img_io.name = 'test.jpg'

url = f'/api/recipe/recipes/{recipe.id}/upload-image/'
res = client.post(url, {'image': img_io}, format='multipart')

print("Upload Response:", res.status_code, res.data)

recipe.refresh_from_db()
print("Recipe Image URL:", recipe.image.url if recipe.image else None)

# Clean up
if recipe.image:
    image_path = recipe.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
