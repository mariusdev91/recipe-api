from django.contrib import admin
from django import forms

from recipe_hub.apps.recipe.models import \
    Recipe, RecipeType, Author, Review
from recipe_hub.apps.recipe.utils.review_utils import ReviewLinkDisplay


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    ingredients = forms.JSONField(
        widget=forms.Textarea(attrs={'class': 'ingredients-json-input'})
    )

    preparation_time = forms.DurationField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter duration '
                                  '(e.g., 1:30:00 for 1 hour 30 minutes)'})
    )

    cooking_time = forms.DurationField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter duration '
                                  '(e.g., 1:30:00 for 1 hour 30 minutes)'})
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_display_reviews',)
    readonly_fields = ('custom_display_reviews',)
    form = RecipeAdminForm

    def custom_display_reviews(self, obj):
        return ReviewLinkDisplay.get_review_links(obj)

    custom_display_reviews.short_description = "Reviews"


class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('recipe_count',)


admin.site.register(RecipeType)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Review)
