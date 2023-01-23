from django.db import models

# Create your models here.
class Home(models.Model ):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    date = models.DecimalField(decimal_places=2, max_digits=10000)
    contact = models.TextField()
