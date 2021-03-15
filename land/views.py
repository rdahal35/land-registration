from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

from .forms import PropertyForm
from .models import Property

class PropertyRegisterView(LoginRequiredMixin,TemplateView):

    template_name = "property-register.html"
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyRegisterView, self).get_context_data(**kwargs)
        context["form"] = PropertyForm(self.request.POST or None)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        if context["form"].is_valid():
            longitude = form.cleaned_data.pop("longitude")
            latitude = form.cleaned_data.pop("latitdude")
            coordinate = [longitude, latitude]
            my_property = form.save(commit=False)
            my_property.user = request.user
            my_property.coordinate = coordinate
            my_property.save()
        # return redirect("/property-register/")
        return super(TemplateView, self).render_to_response(context)

class PropertyView(LoginRequiredMixin, TemplateView):
    template_name = "my-property.html"
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyView, self).get_context_data(**kwargs)
        context["properties"] = Property.objects.filter(user= self.request.user)
        print(context['properties'])
        return context