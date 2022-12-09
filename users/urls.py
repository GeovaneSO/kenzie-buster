from django.urls import path
from . import views
from rest_framework_simplejwt import views as views_jwt
urlpatterns = [
    path("users/login/", views_jwt.TokenObtainPairView.as_view()),
    path("users/login/refresh/", views_jwt.TokenRefreshView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserViewDetails.as_view())
]
