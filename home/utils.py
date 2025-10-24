from django.core.mail 
import send_mailfrom django.core.exceptions 
import ValidationErrorfrom django.core.validators 
import validate_email
def send_email_util(recipient_email, subject, message):    
"""    
Utility function to send an email.    
:param recipient_email: str - recipient email address    
:param subject: str - email subject    
:param message: str - email body    
"""    
try:        
    # Validate email        
    validate_email(recipient_email)        
    # Send email using Django's send_mail function        
    send_mail(            
        subject,            
        message,            
        'no-reply@yourdomain.com',  
        # Replace with your configured sender email            
        [recipient_email],            
        fail_silently=False,        
        )        
        return True  
        # Email sent successfully    
        except ValidationError:        
            print(f"Invalid email address: {recipient_email}")        
            return False    
            except Exception as e:        
                print(f"Error sending email: {e}")        
                return False")