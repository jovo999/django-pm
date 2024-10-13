from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms



class projectlistview(ListView):
    model = models.project
    template_name = 'project/list.html'

class projectcreateview(CreateView):
    model = models.project
    form_class = forms.projectcreateform
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')

