from django.urls import path
from django.http import JsonResponse
from datetime import datetime, timezone

def index(request):
    utc_now = datetime.now(timezone.utc)
    data = {
        "email": "amaechijude178@gmail.com",
        "current_datetime": f"{utc_now.isoformat(timespec='hours')}Z".replace('+', ':'),
        "github_url": "https://github.com/amaechijude/Hng12_backend_stage0"
    }
    return JsonResponse(data)

urlpatterns = [path('', index),]
