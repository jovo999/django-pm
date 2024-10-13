from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.

class projectstatus(models.IntegerChoices):
    PANDEING = 1 , 'pandeing'
    COMPLETED = 2 ,'completed'
    POSTPONED = 3, 'postponed'
    CANCELED = 4 , 'canceled'



class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class project(models.Model):
    title = models.CharField(max_length=255)
    descreption = models.CharField(max_length=255)
    statue = models.IntegerField(
        choices=projectstatus.choices,
        default=projectstatus.PANDEING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category , on_delete=models.PROTECT)
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE , null=True)


    def __str__(self):
        return self.title
    

class task(models.Model):
    descrption = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.descrption




