import secrets
import stringfrom .models 
import Order  
# Adjust this import if your model name/path is different
def generate_unique_order_id(length=10):    
    """Generate a unique, secure alphanumeric ID for an order."""    
    characters = string.ascii_uppercase + string.digits    
    
    while True:        
        # Generate a random string using the secrets module        
        new_id = ''.join(secrets.choice(characters) for _ in range(length))        
        # Check if this ID already exists in the database        
        if not Order.objects.filter(order_id=new_id).exists():            
            return new_id