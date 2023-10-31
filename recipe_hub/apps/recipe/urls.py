from django.urls import path
from recipe_hub.apps.recipe.views import \
    ListCreateRecipeView, ListCreateRecipeTypeView

app_name = 'recipe_hub_recipe'
urlpatterns = [
    path('recipe/',
         ListCreateRecipeView.as_view(),
         name='recipe-list-create'),
    path('recipe-type/',
         ListCreateRecipeTypeView.as_view(),
         name='recipe-type-list-create')

]
