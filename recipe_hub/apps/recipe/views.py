from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from recipe_hub.apps.recipe.models import Recipe, RecipeType
from recipe_hub.apps.recipe.serializers import \
    RecipeSerializer, RecipeTypeSerializer


class ListCreateRecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return super().get_permissions()

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
