from django.test import TestCase
from recipes.models import Category, User, Recipe

class RecipeTestBase(TestCase):
  def setUp(self):
    return super().setUp()
  
  def make_category(self, name='Category'):
    return Category.objects.create(name=name)
  
  def make_author(
      self,
      first_name='user',
      last_name='userlast',
      username='user',
      email='user@email.com',
      password='123456'
    ):
    return User.objects.create_user(
      first_name=first_name,
      last_name=last_name,
      username=username,
      email=email,
      password=password
    )
    
  def make_recipe(
      self,
      title='Recipe title',
      description='Recipe description',
      slug='recipe-slug',
      preparation_time=10,
      preparation_time_unit='Minutos',
      servings=5,
      servings_unit='Porções',
      preparation_steps='recipe preparation steps',
      preparation_steps_is_html=False,      
      is_published=True,
      category=None,
      author=None
    ):
    return Recipe.objects.create(
      title=title,
      description=description,
      slug=slug,
      preparation_time=preparation_time,
      preparation_time_unit=preparation_time_unit,
      servings=servings,
      servings_unit=servings_unit,
      preparation_steps=preparation_steps,
      preparation_steps_is_html=preparation_steps_is_html,      
      is_published=is_published,
      category=category or self.make_category(),
      author=author or self.make_author()
    )