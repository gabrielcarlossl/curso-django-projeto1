from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
  def setUp(self):
    self.recipe = self.make_recipe()
    
    return super().setUp()
  
  def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
    """Test if title has more than 65 chars"""
    
    self.recipe.title = '7' * 70
    
    with self.assertRaises(ValidationError):
      self.recipe.full_clean()
    
    