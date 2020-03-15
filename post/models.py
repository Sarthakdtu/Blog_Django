from django.db import models
import random, string
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

COLOURS = (
    ("success", "Green"),
    ("primary", "Blue"),
    ("danger", "Red"),
    ("warning", "Yellow"),
    ("info", "Cyan"),
    ("secondary", "Grey"),
    ("dark", "Black"),
)


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    colour = models.CharField(max_length=25, choices=COLOURS, default="btn-outline-success")
    colour_outline = models.CharField(max_length=25, null=True, blank=True)
   
    def __str__(self):
        return self.category_name
    
    def clean(self):
        super(Category, self).clean()
        self.category_name = self.category_name.replace(" ", "_")
        self.colour_outline = "btn-outline-" +  self.colour
        self.colour = "btn-" + self.colour
        

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    text = RichTextUploadingField(null=False)
    created_on = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, blank=True, related_name="category")
    tags = models.CharField(max_length=300, null=True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=600, null=True)
    
    def __str__(self):
        return self.title

    def clean(self):
        if not self.tags:
            self.tags = ""
        if not self.title in self.tags:
            self.tags = self.tags + " " + self.title 
    
    

    



