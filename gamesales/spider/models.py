from django.db import models

# Create your models here.

class GameSale(models.Moldel):
    """
    Model to store the game sales
    """

    title = models.Charfield(max_length=200)
    sale_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    release_date = models.DateField()

