from django.db import models
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from model_utils.models import TimeStampedModel

from recipe_hub.apps.recipe.models.author import Author


class Recipe(TimeStampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_history = models.TextField(blank=True)
    recipe_type = models.ForeignKey(
        'RecipeType',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    ingredients = models.JSONField(null=False, blank=False)
    description = models.TextField(max_length=250, blank=True)
    preparation_time = models.DurationField()
    cooking_time = models.DurationField()
    number_of_portions = models.SmallIntegerField(blank=False,
                                                  null=False,
                                                  default=1)
    image = models.ImageField(upload_to='recipe_images/', blank=True)
    rating = models.DecimalField(
        # Allows values up to 9.9; change to 3 for up to 99.9, etc.
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True,  # Allows the rating to be optional
        help_text='Rating from 1.0 to 5.0'
    )

    def __str__(self):
        return f"Recipe {self.title}" \
               f" is of type {self.recipe_type}" \
               f" is cooked in {self.cooking_time}" \
               f" and it serves {self.number_of_portions} persons."

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


@receiver(post_save, sender=Recipe)
def update_recipe_count_on_save(sender, instance, created, **kwargs):
    if created:
        Author.objects.filter(pk=instance.author.pk) \
            .update(recipe_count=F('recipe_count') + 1)


@receiver(post_delete, sender=Recipe)
def update_recipe_count_on_delete(sender, instance, **kwargs):
    Author.objects.filter(pk=instance.author.pk).update(
        recipe_count=F('recipe_count') - 1)
