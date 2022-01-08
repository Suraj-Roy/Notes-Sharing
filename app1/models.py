from django.db import models
from django.contrib.auth.models import User
from .choice import filetype,branchchoice,statuschoice

# Create your models here.
class SignUp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo=models.ImageField(upload_to='profile',default='Profile/R.png')

    def __str__(self):
        return self.user.username

class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=50,choices=branchchoice)
    subject = models.CharField(max_length=50)
    notesfile=models.FileField(upload_to='Notes')
    filetype=models.CharField(max_length=50,choices=filetype)
    description=models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(max_length=15,default="Pending")

    def __str__(self):
        return self.user.username 
    