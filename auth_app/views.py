from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class EditView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/auth/login/'
    template_name='auth_app/edit.html'
    


def signup_page(request):
    if request.method == "GET":
        data = {
            "form": UserCreationForm()
        }
        return render(request, 'registration/signup.html', context=data)

    elif request.method == "POST":
        try:
            form = UserCreationForm(request.POST)
            form.save()
            return redirect("login")
        except ValueError:
            data = {
                "form": form
            }
            return render(request, 'registration/signup.html', context=data)

       
