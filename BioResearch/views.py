from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import *
from BioResearch.forms import PapersForm

templates=loader.get_template('templates.html')

# Create your views here.
def papers_index(request: HttpRequest) -> HttpResponse:
    if request.GET.get('title', False):
        title= request.GET['title']
        paper=Paper.objects.filter(title__icontains=title)
    else:

        paper = Paper.objects.all() 
    return render(request, 'papers_index.html', {"papers" : paper})
    

def new_paper(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":    
        form= PapersForm(request.POST)
        if not form.is_valid():
            return render(request,
            'papers_form.html',
            {"Error":"Something unexpected happened",
            "form": form}
            )   
        new_paper=Paper(**form.cleaned_data)    
        new_paper.save()

        return redirect('bioresearch-index')

    
    else:
        return render(request,'papers_form.html', {"form": PapersForm() })

def papers_search(request: HttpRequest) -> HttpResponse:
    searchpaper = SearchPaper.objects.all()
    return render(request, 'papers_search.html', {"searchpapers" : searchpaper})

def home(request: HttpRequest) -> HttpResponse:
    biohome = Home.objects.all()
    return render(request, 'home.html', {"bioresearch_home" : biohome})
