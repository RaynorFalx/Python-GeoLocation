from django.db import models

# Create your models here.

class Localization(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=50)

    def __str__(self):
        return self.address


class Target(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    picture = models.ImageField(upload_to='imgs')
    localization = models.ForeignKey(Localization,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


