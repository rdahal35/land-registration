from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

PROPERTY_TYPE = (
    ("LA", "Land"),
    ("HO", "House")
)

class Property(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    owner_name = models.CharField(_("Owner Full Name"), max_length=250)
    address = models.CharField(_("Address"), max_length=250)
    contact_no = models.CharField(_("Contact Number"), max_length=250)
    coordinate = ArrayField(models.FloatField(max_length=10, blank=True),size=2)
    area = models.FloatField(_("Area in Sqr ft"), max_length=50)
    floor_numbers = models.IntegerField(_("Number of floors"), null=True, blank=True)
    property_type = models.CharField(_("Property Type"),choices= PROPERTY_TYPE, max_length=2, default="HO")

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self):
        return "{}".format(self.owner_name)

    def get_absolute_url(self):
        return reverse("Property_detail", kwargs={"pk": self.pk})
