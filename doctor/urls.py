from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DesignationViewSet, SpecializationViewSet, AvailableTimeViewSet, DoctorViewSet, ReviewViewSet

router = DefaultRouter()

router.register('designation', DesignationViewSet)
router.register('specialization', SpecializationViewSet)
router.register('available_time', AvailableTimeViewSet)
router.register('list', DoctorViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]