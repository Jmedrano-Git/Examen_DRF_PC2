from rest_framework.routers import DefaultRouter
from .views import GameViewSet, CompanyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='games')
router.register(r'companies', CompanyViewSet, basename='companies')

urlpatterns = [
    path('v1/', include(router.urls)),
]