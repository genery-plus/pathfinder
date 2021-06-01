from django.shortcuts import render
from .models import character
from .forms import CharacterForm



def saveforms (request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect("saveforms")
    return render(request,"main.html",{form: form})

def index (request):
    return  render(request,"index.html",{})