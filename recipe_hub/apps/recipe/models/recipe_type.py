from django.db import models


class RecipeType(models.Model):
    RECIPE_TYPE_NAME = (
        ('1', 'Sweets'),
        ('2', 'Breakfast'),
        ('3', 'Lunch'),
        ('4', 'Dinner'),
        ('5', 'Snack')
    )
    type = models.CharField(max_length=128, choices=RECIPE_TYPE_NAME)

    def __str__(self):
        for choice in self.RECIPE_TYPE_NAME:
            if choice[0] == self.type:
                return choice[1]
        return self.type
