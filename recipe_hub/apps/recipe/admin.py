from django.contrib import admin
from django import forms

from recipe_hub.apps.recipe.models import Recipe, RecipeType


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    ingredients = forms.JSONField(
        widget=forms.Textarea(attrs={'class': 'ingredients-json-input'})
    )
    cooking_time = forms.DurationField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter duration '
                                  '(e.g., 1:30:00 for 1 hour 30 minutes)'})
    )


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeType)
