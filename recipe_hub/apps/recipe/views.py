from rest_framework import generics, status
from rest_framework.response import Response

from recipe_hub.apps.recipe.models import Recipe, RecipeType, Review, Author
from recipe_hub.apps.recipe.serializers import \
    RecipeSerializer, RecipeTypeSerializer, ReviewSerializers, \
    AuthorSerializers
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


class ListCreateReviewView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializers

    def post(self, request, *args, **kwargs):
        context = {
            'user': request.user,
            'recipe': request.data.get('recipe'),
            'text': request.data.get('text')
        }
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ListCreateAuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    def post(self, request, *args, **kwargs):
        context = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'social_media_account': request.data.get('social_media_account')
        }
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
