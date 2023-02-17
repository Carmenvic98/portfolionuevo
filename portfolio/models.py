from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to="portfolio/images/")
    description = CharField(max_length=1000)
    url = URLField(blank=True)
