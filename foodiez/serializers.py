from rest_framework import serializers
from .models import Category, Recipie, Ingredient



class IngredientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    ingredient_set = IngredientListSerializer(many=True, read_only=True)

    class Meta:
        model = Recipie
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    recipie_set = RecipeListSerializer(source= 'recipies',many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    recipie_set = RecipeListSerializer(source= 'recipies',many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class RecipeDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    ingredient_set = IngredientListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class IngredientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    