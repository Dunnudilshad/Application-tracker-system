from django.contrib import admin
from django.urls import include, path
from atsapp.views import *

urlpatterns = [
    
    path('',upload_resume_view,name='upload_resume_view'),
    path('delete/<id>',delete)
    
    
]
