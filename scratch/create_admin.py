import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
try:
    if not User.objects.filter(email='admin@example.com').exists():
        User.objects.create_superuser('admin@example.com', 'admin123')
        print("Superuser 'admin@example.com' created successfully!")
    else:
        print("Superuser 'admin@example.com' already exists.")
except Exception as e:
    print(f"Error creating superuser: {e}")
