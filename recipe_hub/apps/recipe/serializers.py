from rest_framework import serializers
from recipe_hub.apps.recipe.models import Recipe, RecipeType


class RecipeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeType
        fields = ['id', 'type']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe_type', 'ingredients', 'cooking_time', 'number_of_portions']
        depth = 1
