from django.db import models
from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=100)
    recipe_type = models.ForeignKey('RecipeType',
                                    on_delete=models.CASCADE,
                                    null=False, blank=False)
    ingredients = models.JSONField(null=False, blank=False)
    cooking_time = models.PositiveIntegerField(blank=False,
                                               null=False,
                                               default=1)
    number_of_portions = models.SmallIntegerField(blank=False,
                                                  null=False,
                                                  default=1)

    def __str__(self):
        return f"Recipe called {self.name}"\
               f" is of type {self.recipe_type}"\
               f" is cooked in {self.cooking_time}"\
               f" and it serves {self.number_of_portions} persons."
