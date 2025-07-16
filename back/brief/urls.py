from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BriefViewSet

router = DefaultRouter()
router.register(r'briefs', BriefViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
