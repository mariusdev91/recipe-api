from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Review(TimeStampedModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reviews')
    recipe = models.ForeignKey('Recipe',
                               related_name='reviews',
                               on_delete=models.CASCADE)
    text = models.TextField(max_length=150)

    def __str__(self):
        return f"Review by {self.user.username}"
