from rest_framework import generics, status
from rest_framework.response import Response

from recipe_hub.apps.recipe.models import Recipe, RecipeType
from recipe_hub.apps.recipe.serializers import \
    RecipeSerializer, RecipeTypeSerializer
from recipe_hub.apps.recipe.utils.permissions import IsAuthenticatedOrNotFound


class ListCreateRecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrNotFound]

    def post(self, request, *args, **kwargs):
        context = {
            "recipe_type": request.data.get('recipe_type')
        }
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListCreateRecipeTypeView(generics.ListCreateAPIView):
    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer
