from django.shortcuts import render
from django.views import generic
from main.models import PersonModel


class ShowPerson(generic.ListView):
    model = PersonModel
