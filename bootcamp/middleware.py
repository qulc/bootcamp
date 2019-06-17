from django.core import signing
from django.contrib.auth.models import User

from django.utils.deprecation import MiddlewareMixin


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        authorization: str = request.META.get('HTTP_AUTHORIZATION')
        if not authorization or not authorization.startswith('JWT'):
            return

        _, token = authorization.split()
        try:
            user_id = signing.loads(token)
        except signing.BadSignature:
            return

        if not user_id or not isinstance(user_id, int):
            return

        request.user = User.objects.get(id=user_id)
