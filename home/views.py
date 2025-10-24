def homepage_view(request):    
    context = {        
        "restaurant_name": "Tasty Bites",        
        "welcome_message": "Welcome to Tasty Bites! We are glad to have you here.",        
        "opening_hours": "Mon–Fri: 11am–9pm, Sat–Sun: 10am–10pm"    
        }    
        return render(request, "home/homepage.html", context);
        name='available_tables_api';
        calculate_total