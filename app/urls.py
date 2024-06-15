from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, FriendshipViewSet, MessageViewSet, PostViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')
router.register('friendship', FriendshipViewSet, basename='friendship')
router.register('message', MessageViewSet, basename='message')
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]