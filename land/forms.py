from django import  forms
from .models import Property, PROPERTY_TYPE


class PropertyForm(forms.ModelForm):
    longitude = forms.FloatField( required=False)
    latitdude = forms.FloatField(required=False)
    property_type = forms.ChoiceField(
        choices = PROPERTY_TYPE, label="Property Type", initial='HO', widget=forms.Select(), required=True
        )
    class Meta:
        model = Property
        fields = ["owner_name", "address", "contact_no", "longitude","latitdude", "area", "floor_numbers"]
