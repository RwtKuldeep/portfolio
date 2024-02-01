from django.shortcuts import render
from .models import User
from .forms import Registration
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":
        fm = Registration(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            pw = fm.cleaned_data['password']
            mg = fm.cleaned_data['messages']
            reg = User(name=nm, email=em, password=pw,
                       messages=mg, age=ag)
            reg.save()
            messages.success(request, 'Your Data Added Successfully!!!')
            fm = Registration()
    else:
        fm = Registration()
    return render(request, 'staticwebpage.html', {'form': fm})
