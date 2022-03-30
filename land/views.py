from importlib.resources import contents
from django.shortcuts import render, redirect
import uuid
# import hashlib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages

from users.models import User

from .forms import PropertyForm
from .models import Property, Survey

from .owner import create_owner
from .utils import generate_sha256
from .contract import register_asset, get_asset


class PropertyRegisterView(LoginRequiredMixin, TemplateView):

    template_name = "property-register.html"
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyRegisterView, self).get_context_data(**kwargs)
        context["form"] = PropertyForm(self.request.POST or None)
        context['link'] = "reg-prop"

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        if context["form"].is_valid():
            longitude = form.cleaned_data.pop("longitude")
            latitdude = form.cleaned_data.pop("latitdude")
            coordinate = [longitude, latitdude]
            my_property = form.save(commit=False)
            my_property.user = request.user
            my_property.coordinate = coordinate
            hash = generate_sha256(my_property)
            print(hash.hexdigest())
            my_property.sha256 = hash.hexdigest()
            my_property.save()
            survey = Survey.objects.create(prty=my_property)
        return redirect("/property/")
        # return super(TemplateView, self).render_to_response(context)


class PropertyView(LoginRequiredMixin, TemplateView):
    template_name = "my-property.html"
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyView, self).get_context_data(**kwargs)
        context["properties"] = Property.objects.filter(
            user=self.request.user)[::-1]
        print(context['properties'])
        context['link'] = 'prop'
        # generate_sha256(context["properties"][0])
        return context


class PropertyDetailView(LoginRequiredMixin, TemplateView):
    template_name = "land/property-detail.html"
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)
        context["property"] = Property.objects.get(id=self.kwargs.get("id"))
        property = context['property']
        print(property.survey.survey_id)
        asset = get_asset(int(property.id))
        # print(asset)
        if asset[4] == property.sha256:
            context["valid"] = True
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["link"] = "das"
        print(User.objects.filter(is_active=False).count())
        context["users"] = {
            "active": User.objects.filter(is_superuser=False, is_active=True).count(),
            "inactive": User.objects.filter(is_active=False).count()
        }
        context["property"] = {
            "pending": Property.objects.filter(status="P").count(),
            "accepted": Property.objects.filter(status="A").count()
        }
        return context


class UsersView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_superuser=False)
        context["link"] = "usr"
        return context


class AdminProperties(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/properties.html"

    def get_context_data(self, **kwargs):
        context = super(AdminProperties, self).get_context_data(**kwargs)
        context['properties'] = Property.objects.all().order_by("-id")
        context["link"] = "prop"
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        survey_no = request.POST.get("survey_no")
        status = request.POST.get("status")
        property = Property.objects.get(id=id)
        survey = Survey.objects.get(prty=property)
        print(property.survey.survey_id,
              survey.survey_id, survey.prty.owner_name)

        if survey_no != "" and survey_no == str(survey.survey_id):
            property.status = status
            property.survey_no = survey_no
            print(status)

            if property.status == "A":
                uuid = str(property.sha256)
                survey_no = int(survey.id)
                owner_address = str(property.user.public_address)
                owner_id = str(property.user.id)
                sha256 = str(property.sha256)
                id = int(property.id)
                district = str(property.district)
                print(uuid, survey_no, owner_address,
                      owner_id, sha256, id, district)

                register_asset(uuid, survey_no, owner_address,
                               owner_id, sha256, id, district)
            property.save()
        else:
            messages.error(request, 'Invalid Survey number!')

        return redirect("dashboard-properties")
