from django.db import models
import uuid
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places  = 2, default = None)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Books'
