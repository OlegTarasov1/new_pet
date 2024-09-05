from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from . import views

notes_router = routers.SimpleRouter()
notes_router.register(r'notes', views.NoteMeneger)

urlpatterns = [
    path('api/v1/', include(notes_router.urls)),
    path('api/v1/uuid/', views.CreateUuid.as_view()),
]