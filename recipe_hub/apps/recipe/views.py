from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from recipe_hub.apps.recipe.models import Recipe, RecipeType
from recipe_hub.apps.recipe.serializers import RecipeSerializer, RecipeTypeSerializer


class ListCreateRecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return super().get_permissions()


class ListCreateRecipeTypeView(generics.ListCreateAPIView):
    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer

