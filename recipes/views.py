from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import HttpResponse
from django.http import Http404

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
    
    # recipes = Recipe.objects.filter(
    #         category__id=category_id,
    #         is_published=True
    #     ).order_by('-id')
    
    
    # Opção de Mostrar pagina não encontrada 
        
    # category_name = getattr(
    #     getattr(recipes.first(), 'category', None),
    #     'name',
    #     'Not Found'
    # )
    
    # if not recipes:
        # return HttpResponse(content='Not Found', status=404)
        
        # Usando padrão do Django        
        # raise Http404('Not found ')
        
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )
        
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | ' 
    })

def recipe(request, id):
    # recipe = Recipe.objects.get(id=id)
    # title =  Recipe.objects.get(id=id).title
    
    # recipe = Recipe.objects.filter(
    #     pk=id,
    #     is_published=True
    # ).order_by('-id').first()
    
    # return render(request, 'recipes/pages/recipe-view.html', context={
    #     'recipe': make_recipe(),
    #     'is_detail_page': True
    # })
    
    ## Retorna erro 404 se não encontrar o objeto
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True
    )
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
