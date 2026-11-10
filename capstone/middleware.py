from django.conf import settings
from django.http import HttpResponse


class DemoReadOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.VERCEL_DEMO and request.method not in {'GET', 'HEAD', 'OPTIONS'}:
            return HttpResponse(
                'Đây là bản demo giao diện. Chức năng lưu dữ liệu chưa được bật.',
                status=403,
                content_type='text/plain; charset=utf-8',
            )
        return self.get_response(request)
