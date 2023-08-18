from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

# Create your models here.
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Maps', 'Maps'),
        ('Newsletter', 'Newsletter'),
        ('referral', 'referral')
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100, default="null")

    location = models.CharField(max_length=100, default="null")
    
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, default="null", blank=True)
    date_time = models.DateTimeField(auto_now_add=True, help_text='when lead was created.')

    def __str__(self):
        return self.first_name



