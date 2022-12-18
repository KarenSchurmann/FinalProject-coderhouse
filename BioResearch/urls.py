from django.urls import path    
from BioResearch import views



urlpatterns= [
    path("", views.papers_index, name= "bioresearch-index"),
    path("new", views.new_paper, name= "bioresearch-form"),
    path("search", views.papers_search, name= "bioresearch-search"),
    path("home", views.home, name= "bioresearch-home"),
    

]