from django.db import models
from django.contrib.auth import get_user_model

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # location = models.TextField()
    # media = models.TextField() - limit to either film or television
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE,
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name='pledges',
        on_delete=models.CASCADE,
    )
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE,
    )