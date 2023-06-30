# using router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, AboutMeViewSet, SkillViewSet, ContactViewSet, FrontendViewSet, BackendViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='frontend')
router.register('about', AboutMeViewSet, basename='about')
router.register('skill', SkillViewSet, basename='skill')
router.register('contact', ContactViewSet, basename='contact')
router.register('frontend', FrontendViewSet, basename='frontend')
router.register('backend', BackendViewSet, basename='backend')

urlpatterns = [
    path('', include(router.urls))
]