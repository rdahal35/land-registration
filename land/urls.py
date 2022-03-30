from django.urls import path, include

from .views import (PropertyRegisterView, PropertyView,
                    PropertyDetailView, DashboardView, UsersView, AdminProperties)


urlpatterns = [
    path("property-register/", PropertyRegisterView.as_view(),
         name="property-register"),
    path("property/", PropertyView.as_view(), name="property"),
    path("property-detail/<int:id>/",
         PropertyDetailView.as_view(), name='property-detail'),
    path("admin/dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/users/", UsersView.as_view(), name="dashboard-users"),
    path("dashboard/properties/", AdminProperties.as_view(),
         name="dashboard-properties"),
]
