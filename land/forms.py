from django import forms
from .models import Property, PROPERTY_TYPE


class PropertyForm(forms.ModelForm):
    longitude = forms.FloatField(required=False)
    latitdude = forms.FloatField(required=False)
    public_addr = forms.CharField(required=False)

    class Meta:
        model = Property
        fields = ["owner_name", "address", "contact_no",
                  "longitude", "latitdude", "area", "state", "district", "village"]
