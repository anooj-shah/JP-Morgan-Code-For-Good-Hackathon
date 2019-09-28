
from django.db import models

class Representative(models.Model):
    state = models.CharField(max_length = 200)
    fname = models.CharField(max_length = 10)
    lname = models.CharField(max_length = 200)
    party = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    first_elected = models.CharField(max_length = 200)
    next_election = models.CharField(max_length = 200)
    deadlines = models.CharField(max_length = 200)





# Create your models here.
