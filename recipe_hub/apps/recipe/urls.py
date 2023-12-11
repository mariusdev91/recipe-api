from django.urls import path
from recipe_hub.apps.recipe.views import \
    ListCreateRecipeView, ListCreateRecipeTypeView, ListCreateReviewView, \
    ReviewDetailView, ListCreateAuthorView

app_name = 'recipe_hub_recipe'
urlpatterns = [
    path('recipe/',
         ListCreateRecipeView.as_view(),
         name='recipe-list-create'),
    path('recipe-type/',
         ListCreateRecipeTypeView.as_view(),
         name='recipe-type-list-create'),
    path('review/', ListCreateReviewView.as_view(),
         name='review-list-create'
         ),
    path('review/<int:pk>/', ReviewDetailView.as_view(),
         name='review-list'),
    path('author/', ListCreateAuthorView.as_view(),
         name='author-list-create')
]
