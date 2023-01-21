from django.db import models

# Create your models here.
class Home(models.Model ):
    navBar = models.TextField()
    title = models.TextField()
    contact = models.TextField()
    description = models.TextField(default='this is cool')