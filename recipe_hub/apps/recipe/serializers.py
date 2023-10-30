from rest_framework import serializers
from recipe_hub.apps.recipe.models import RecipeType
from drf_extra_fields.fields import Base64ImageField


class RecipeTypeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = RecipeType
        fields = ['id', 'type']

    def get_type(self, obj):
        return obj.get_type_display()


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    short_history = serializers.CharField()
    recipe_type = RecipeTypeSerializer(many=False)
    ingredients = serializers.JSONField()
    description = serializers.CharField()
    cooking_time = serializers.DurationField()
    number_of_portions = serializers.IntegerField()
    image = Base64ImageField(required=False, allow_null=True)


