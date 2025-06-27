from django.db import models
class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return self.firstname
# Create your models here.
