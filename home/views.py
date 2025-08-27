from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request):    
    try:        
        context = {            
            "restaurant_name": "Tasty Bites",            
            "welcome_message": "Welcome to Tasty Bites! We are glad to have you here."        
            }        
            return render(request, "home/homepage.html", context)    
            
            except Exception as e:        
                # Log the error (optional: use logging module instead of print)        
                print(f"Error in homepage_view: {e}")                
                
                # Show a friendly error page        
                return HttpResponse("<h2>Oops! Something went wrong. Please try again later.</h2>")")
