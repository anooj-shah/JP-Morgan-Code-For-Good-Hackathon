from django.db import models
import csv

class Info(models.Model):
    state = models.CharField(max_length = 200)
   # branch = models.CharField(max_length = 200)
    #district = models.CharField(max_length = 200)
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    party = models.CharField(max_length = 200)
    # leadership = models.CharField(max_length = 200)
    # committee = models.CharField(max_length = 200)
    # committee = models.CharField(max_length = 200)
    # committee = models.CharField(max_length = 200)
    # committee = models.CharField(max_length = 200)
    # notes = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
   # briefs = models.CharField(max_length = 200)
    first_elected = models.CharField(max_length = 200)
    next_election = models.CharField(max_length = 200)
    deadlines = models.CharField(max_length = 200)
    # term_limited = models.CharField(max_length = 200)
    # counties_represented = models.CharField(max_length = 200)


# Create your models here.
