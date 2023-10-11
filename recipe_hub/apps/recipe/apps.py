from django.apps import AppConfig


class RecipeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_hub.apps.recipe.models.recipe'
    label = 'recipe_hub_recipe'


class RecipeTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_hub.apps.recipe.models.recipe_type'
    label = 'recipe_hub_recipe_type'
