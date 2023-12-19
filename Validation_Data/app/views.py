from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

def sing_up(request):
    if request.method == "POST":
        name = request.POST.get("name", "Undefined")
        password = request.POST.get("password", "Undefined")

        input_name = InputName(request.POST)
        input_password = InputPassword(request.POST)

        if input_name.is_valid() and input_password.is_valid():
            if name == 'User1' and password == "12345678":
                return render(request, 'app/result.html', context={'text': 'Вы успешно вошли'})

            else:
                return HttpResponseRedirect('sing_in/')


    else:
        input_name = InputName()
        input_password = InputPassword()
        return render(request, 'app/sing_up.html', context={'input_name': input_name, 'input_password': input_password})

def sing_in(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Undefined')
        email = request.POST.get('email', 'Undefined')
        password = request.POST.get('password', 'Undefined')

        input_name = InputName(request.POST)
        input_email = InputEmail(request.POST)
        input_password = InputPassword(request.POST)

        if input_name.is_valid() and input_email.is_valid() and input_password.is_valid():
            return render(request, 'app/result2.html', context={'name': name,'text': ', поздравляю с регистрацией!'})

    else:
        input_name = InputName()
        input_email = InputEmail()
        input_password = InputPassword()
        return render(request, 'app/sing_in.html', context={'input_name': input_name, 'input_email': input_email, 'input_password': input_password})


def user(request):
    return render(request, 'app/result.html')