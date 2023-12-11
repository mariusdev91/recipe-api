from rest_framework import serializers
from recipe_hub.apps.recipe.models import RecipeType, Recipe, Review
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'password']
        extra_kwargs = {'password': {'write_only': True}}


class RecipeTypeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = RecipeType
        fields = ['id', 'type']

    @staticmethod
    def get_type(obj):
        return obj.get_type_display()


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    short_history = serializers.CharField()
    recipe_type = RecipeTypeSerializer(many=False)
    ingredients = serializers.JSONField()
    description = serializers.CharField()
    cooking_time = serializers.DurationField()
    number_of_portions = serializers.IntegerField()
    image = Base64ImageField(required=False, allow_null=True)

    def validate(self, data):
        title = data.get('title')
        if len(title) > 100:
            raise serializers.ValidationError(
                "Title is too long, please provide a shorter title.")
        elif len(title) == 0:
            raise serializers.ValidationError("No title was provided!")

        # Check if the recipe type is a valid choice
        recipe_type_data = self.context.get('recipe_type').get('type')
        if recipe_type_data:
            if any(value for key, value in
                   RecipeType.RECIPE_TYPE_NAME if value == recipe_type_data):
                recipe_type_instance, created = \
                    RecipeType.objects.get_or_create(type=recipe_type_data)
                data['recipe_type'] = self.context.get('recipe_type')
                recipe_type_id = recipe_type_instance.id
                data['recipe_type_id'] = recipe_type_id
            else:
                raise serializers. \
                    ValidationError("Invalid recipe type provided.")

        description = data.get('description')
        if len(description) > 250:
            raise serializers.ValidationError({
                "Description":
                    "The provided description is too long."
            })

        return data

    def create(self, validated_data):
        # Extract and remove the recipe_type_id from validated_data
        recipe_type_id = validated_data.pop('recipe_type_id', None)
        recipe_type = RecipeType.objects.get(id=recipe_type_id)

        # Also remove the original 'recipe_type' entry
        validated_data.pop('recipe_type', None)

        # Now create the Recipe instance
        recipe = Recipe.objects.create(
            recipe_type=recipe_type, **validated_data)
        return recipe


class ReviewSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    recipe = RecipeSerializer(read_only=True)
    text = serializers.CharField()

    def validate(self, data):
        recipe = self.context.get('recipe')
        user = self.context.get('user')

        if recipe and 'id' in recipe:
            recipe_id = recipe['id']
        existing_recipes = Recipe.objects.all().values_list('id', flat=True)

        data['recipe_id'] = recipe_id
        data['user'] = user
        data['text'] = self.context.get('text')

        if recipe_id not in list(existing_recipes):
            raise serializers.ValidationError(
                {'Recipe': [f"Recipe with the id: "
                            f"'{recipe_id}' does not "
                            f"exist in the database."]}
            )

        return data

    def create(self, validated_data):
        recipe_id = validated_data['recipe_id']
        user = validated_data['user']

        created_review = Review.objects.create(
            recipe_id=recipe_id,
            user=user,
            text=validated_data['text'],
        )

        return created_review


class AuthorSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    social_media_account = serializers.URLField()
    recipe_count = serializers.IntegerField(read_only=True)

    def validate(self, data):
        first_name = self.context.get('recipe')
        last_name = self.context.get('user')
        email = self.context.get('recipe')
        social_media_account = self.context.get('social_media_account')

        data['first_name'] = first_name
        data['last_name'] = last_name
        data['email'] = email
        data['social_media_account'] = social_media_account

        

        return data

    def create(self, validated_data):
        recipe_id = validated_data['recipe_id']
        user = validated_data['user']

        created_review = Review.objects.create(
            recipe_id=recipe_id,
            user=user,
            text=validated_data['text'],
        )

        return created_review



