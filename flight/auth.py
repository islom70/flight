from django.http import JsonResponse
from django.conf import settings


def api_key_middleware(get_response):
    def middleware(request):
        api_key = request.headers.get('X-API-KEY')
        if api_key != settings.API_KEY:
            return JsonResponse({'error': 'Forbidden'}, status=403)
        return get_response(request)
    return middleware
