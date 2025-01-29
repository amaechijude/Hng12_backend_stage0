from django.urls import path
from django.http import JsonResponse
from datetime import datetime
import pytz

def index(request):
    current_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
        "email": "amaechijude178@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/amaechijude/Hng12_backend_stage0"
    }
    return JsonResponse(data)

urlpatterns = [path('', index),]
