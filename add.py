"""
Module for adding a list to the JSON data
"""
from ds import Unit, IngredientQty, Recipe

class RecipeAddException(Exception):
    pass

def add_recipe(recipes_path: str, ingr_path: str) -> RecipeAddException | None:
    """
    Obtain recipe information from stdin from the user.
    """
    pass
