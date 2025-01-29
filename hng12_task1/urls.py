"""
URL configuration for hng12_task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import JsonResponse
from datetime import datetime, timezone

def index(request):
 data = {
   "email": "amaechijude178@gmail.com",
   "current_datetime": f"{datetime.now(timezone.utc).isoformat()}",
   "github_url": " https://github.com/amaechijude/Hng12_backend_stage0.git"
 }
 return JsonResponse(data)

urlpatterns = [path('', index),]
