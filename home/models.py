from django.db import models

class ContactFormSubmission(models.Model):    
    name = models.CharField(max_length=100)    
    email = models.EmailField()    
    message = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)    
    def _str_(self):        
        return f"{self.name} - {self.email}"
# Create your models here.
