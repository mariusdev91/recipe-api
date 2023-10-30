from rest_framework import generics
from recipe_hub.apps.recipe.models import Recipe, RecipeType
from recipe_hub.apps.recipe.serializers import RecipeSerializer, RecipeTypeSerializer


class ListCreateRecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ListCreateRecipeTypeView(generics.ListCreateAPIView):
    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer

