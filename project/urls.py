
from django.urls import path , include
from . import views


urlpatterns = [


    path('' , views.projectlistview.as_view() , name = 'project_list'),
    path('project/create' , views.projectcreateview.as_view() , name = 'project_create')

]




