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


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeType)
