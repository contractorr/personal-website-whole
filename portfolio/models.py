from django.db import models

# Create your models here.
class InputsContainer(models.Model):
    """A model to store the messages sent by visitors"""
    starting_amount = models.FloatField(default=5000)
    cagr = models.FloatField(default=20)
    num_years = models.IntegerField(default=20)    
    beginning_year = models.IntegerField(default=2021)
    annual_topup = models.FloatField(default=1000)
    topup_years = models.IntegerField(default=5)