from itertools import chain
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.postgres.fields import ArrayField
from users.models import User
from .utils import generate_sha256

PROPERTY_TYPE = (
    ("LA", "Land"),
    ("HO", "House")
)

STATUS = (
    ("P", "Pending"),
    ("D", "Declined"),
    ("A", "Accepted")
)


class Property(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), on_delete=models.CASCADE)
    owner_name = models.CharField(_("Owner Full Name"), max_length=250)
    state = models.CharField(_("State"), max_length=200, null=True)
    district = models.CharField(_("District"), max_length=200)
    municiplity = models.CharField(
        _("Municiplity"), max_length=200, null=True, blank=True)
    village = models.CharField(
        _("Village"), max_length=200, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=250)
    contact_no = models.CharField(_("Contact Number"), max_length=250)
    coordinate = ArrayField(models.FloatField(
        max_length=10, blank=True), size=2)
    area = models.FloatField(_("Area in Sqr ft"), max_length=50)
    sha256 = models.CharField(
        _("Sha256"), null=True, blank=True, max_length=100)
    status = models.CharField(
        _("Status"), max_length=1, choices=STATUS, default="P")
    survey_no = models.CharField(
        _("Survey Number"), max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Property.objects.get(pk=self.pk)
            if orig.user != self.user or orig.owner_name != self.owner_name or orig.coordinate != self.coordinate or orig.area != self.area:
                sha256 = generate_sha256(self)
                self.sha256 = sha256.hexdigest()

        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.owner_name)

    def get_absolute_url(self):
        return reverse("Property_detail", kwargs={"pk": self.pk})


class Survey(models.Model):

    survey_id = models.UUIDField(default=uuid.uuid4, editable=False)
    prty = models.OneToOneField(Property, verbose_name=_(
        "Property"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")

    def __str__(self):
        print(self.survey_id)
        return str(self.prty.id) + "-" + str(self.prty.owner_name)

    def get_absolute_url(self):
        return reverse("Survey_detail", kwargs={"pk": self.pk})
