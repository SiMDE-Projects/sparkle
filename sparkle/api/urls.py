from django.urls import include, path
from rest_framework import routers

api_router = routers.DefaultRouter()

urlpatterns = [
    path("", include(api_router.urls)),
]
