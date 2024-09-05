from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from . import views

user_router = routers.SimpleRouter()
user_router.register(r'profile', views.UserBase)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/v1/user_manip/', include(user_router.urls)),
    # path('accounts/', include('allauth.urls')),
]