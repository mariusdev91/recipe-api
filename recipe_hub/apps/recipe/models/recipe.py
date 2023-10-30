from django.db import models
from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    title = models.CharField(max_length=100)
    short_history = models.TextField(blank=True)
    recipe_type = models.OneToOneField(
                    'RecipeType',
                    on_delete=models.CASCADE,
                    null=False,
                    blank=False
                 )
    ingredients = models.JSONField(null=False, blank=False)
    description = models.TextField(max_length=250, blank=True)
    cooking_time = models.DurationField()
    number_of_portions = models.SmallIntegerField(blank=False,
                                                  null=False,
                                                  default=1)
    image = models.ImageField(upload_to='media_root/', default="", blank=True)

    def __str__(self):
        return f"Recipe called {self.title}" \
               f" is of type {self.recipe_type}" \
               f" is cooked in {self.cooking_time}" \
               f" and it serves {self.number_of_portions} persons."
