from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet, LoginAPI
from rest_framework import routers

# Initialize the router
router = routers.DefaultRouter()

# Register viewsets with the router
router.register(r'companies', CompanyViewSet, basename='company')  # Manually specify basename
router.register(r'employees', EmployeeViewSet, basename='employee')  # Manually specify basename

urlpatterns = [
    path("", include(router.urls)),  # Include router URLs
    path("login/", LoginAPI.as_view()),  # Add the login API view
]
