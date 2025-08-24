from django.shortcuts import render

def homepage_view(request):    
    context = {        
        'restaurant_name': 'Tasty Bites',        
        'welcome_message': 'Welcome to Tasty Bites! We are glad to have you here.'    
        }    
        return render(request, 'home/homepage.html', context)
