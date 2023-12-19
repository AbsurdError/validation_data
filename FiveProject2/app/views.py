from django.shortcuts import render, redirect
from .forms import UserForm #UserForm2
from django.http import HttpResponse
from .models import Person

# Create your views here.

def getData(request):
    tom = Person.objects.get_or_create(name='Tom', age=25, photo='bbv.ipg')
    mike = Person(name='Mike', age=15, photo='fghj.jpg')
    mike.save()
    people = Person.objects.all()
    # people = Person.objects.filter(age=20)
    # return HttpResponse(people)
    return render(request, 'app/data.html', context={'data': people})


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
        # name = request.POST.get('name')
            return HttpResponse(f'Name: {name}')
        else:
            return HttpResponse(f'Данные не валидны')
    else:
        form = UserForm()
        # form2 = UserForm2()
        # return render(request, 'app/index.html', context={'form': form, 'form2': form2})
        return render(request, 'app/index.html', context={'form': form})