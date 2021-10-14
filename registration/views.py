from django.shortcuts import render

# импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

# функция reverse_lazy позволяет получить URL по параметру "name" функции path()
# берём, тоже пригодится
from django.urls import reverse_lazy

# импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')  # где login — это параметр "name" в path()
    template_name = "registration.html"


#login - вход
from django.shortcuts import render
from .forms import Signupform, Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def pagelogin(request):
    uservalue = ''
    passwordvalue = ''

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form,
                       'error': 'The login has been successful'}

            return render(request, 'siteusers/login.html', context)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}

            return render(request, 'siteusers/login.html', context)

    else:
        context = {'form': form}
        return render(request, 'siteusers/login.html', context)


