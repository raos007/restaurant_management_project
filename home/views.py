from django.conf import settings
from django.shortcuts import render

def homepage_view(request):    
    context = {        
        'phone_number': settings.RESTAURANT_PHONE_NUMBER    
        }    
        return render(request, 'home/homepage.html', context)
