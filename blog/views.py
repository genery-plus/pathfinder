from django.shortcuts import render, redirect
from .models import character
from .forms import CharacterForm



def saveforms (request):
    form = CharacterForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        a = form.save(commit=False)
        a.save()
        return redirect("saveforms")
    return render(request,"./main.html", {form: form})

def index (request):
    return  render(request,"index.html",{})


#страница main
def main (request):
    return  render(request,"main.html",{})