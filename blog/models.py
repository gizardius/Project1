from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image= models.ImageField(upload_to='')
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)