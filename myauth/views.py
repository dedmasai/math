from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here.
class AboutMeView(TemplateView):
        template_name = 'myauth/about-me.html'

class RegisterView(CreateView):
        form_class = UserCreationForm
        template_name = 'myauth/register.html'
        success_url = reverse_lazy('myauth:about-me')
        def form_valid(self, form):
                response = super().form_valid(form)
                username =form.cleaned_data.get("username")
                password =form.cleaned_data.get("password1")
                user = authenticate(
                        self.request,
                        username=username,
                        password=password,
                )
                login(request=self.request,user=user)
                return response