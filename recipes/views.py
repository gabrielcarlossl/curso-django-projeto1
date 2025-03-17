from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    
    # Exibindo as receitas por ordem decrescente que estão publicadas
    
    
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    
    # Usando o faker para gerar 10 receitas
    # return render(request, 'recipes/pages/home.html', context={
    #     'recipes': [make_recipe() for _ in range(10)]
    # })
    
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })
    
    
def category(request, category_id):
    
    # Exibindo receitas que tem a mesma categoria
    
    recipes = Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes
    })

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    # return render(request, 'recipes/pages/recipe-view.html', context={
    #     'recipe': make_recipe(),
    #     'is_detail_page': True
    # })
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
