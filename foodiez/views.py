from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ingredient, Recipie, Category
from .serializers import CategoryDetailSerializer, CategoryListSerializer, RecipeListSerializer, IngredientListSerializer, RecipeDetailSerializer,IngredientDetailSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'
    


class RecipeListView(ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipeListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = RecipeDetailSerializer
    lookup_field = 'id'


class IngredientListView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer

class IngredientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = IngredientDetailSerializer
    lookup_field = 'id'


