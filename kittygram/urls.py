from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcat')
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
