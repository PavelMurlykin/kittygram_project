from django.urls import path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
]
