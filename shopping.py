"""
Module to read and process data, given input arguments, from 
"""
from typing import List

from ds import Unit, IngredientQty, Recipe

def make_shopping_list(days: int, recipes_path: str, ingr_path: str) -> List[Recipe]:
    """
    Entry into the main recipe-searching/list-generating part of the application
    """
    # FIXME: Dummy data for now (this is for a simple stub)
    return [Recipe("Butter Chicken", [IngredientQty("Chicken", 2000, Unit.GRAMS, 12)])]
