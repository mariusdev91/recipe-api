from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_hub.apps.user'
    label = 'recipe_hub_user'
