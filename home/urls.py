from django.urls import path
from django.conf.urls import handler404
from.import views

urlpatterns = [
    
]

handler404 = 'your_project_name.views.custom_404'