from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', views.PostViewSet)
v1_router.register(r'groups', views.GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment'
)
v1_router.register(r'follow', views.FollowViewSet, basename='follow')

jwt_routers = [
    path('jwt/create/', TokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name="jwt-verify"),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include(jwt_routers)),
]
