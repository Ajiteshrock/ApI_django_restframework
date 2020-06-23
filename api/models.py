from django.db import models

# Create your models here.
 
# Create your models here.
class user(models.Model):
   
    user_name = models.CharField(max_length=128)
    user_id = models.IntegerField()
    user_startdate = models.DateField(max_length=240)
    user_end_date = models.DateField(max_length=250)
    user_tz = models.CharField(max_length = 250)
