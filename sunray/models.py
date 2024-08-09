

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_details = models.TextField(default='')
    image = models.ImageField(upload_to='projects')  # Assuming you upload images to 'media/projects'
    date_created = models.DateField(auto_now_add=True)
    # Add any other fields you need

    def __str__(self):
        return self.title


class LargeProject(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50,default='')
    description = models.TextField()
    image = models.ImageField(upload_to='large_projects')  # Upload image to 'media/large_projects'
    date_created = models.DateField(auto_now_add=True)
    project_details = models.TextField()  # Additional field for project details

    def __str__(self):
        return self.title
    
    
class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name