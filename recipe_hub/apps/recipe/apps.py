from django.apps import AppConfig


class RecipeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_hub.apps.recipe'
    label = 'recipe_hub_recipe'
