from django.urls import path, include

from .views import PropertyRegisterView, PropertyView


urlpatterns = [
    path("property-register/", PropertyRegisterView.as_view(), name="property-register"),
    path("property/", PropertyView.as_view(), name="property"),
]
