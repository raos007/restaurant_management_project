from django.urls import path
from .views import homepage_view, feedback_view

urlpatterns = [    
    path('', homepage_view, name='homepage'),    
    path('feedback/', feedback_view, name='feedback'),
    ]
