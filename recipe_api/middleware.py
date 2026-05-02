from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

class AutoLoginMiddleware(MiddlewareMixin):
    """Automatically log in the first user for local development testing."""
    def process_request(self, request):
        if not request.user.is_authenticated:
            User = get_user_model()
            user = User.objects.first()
            if user:
                request.user = user
