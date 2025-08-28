from typing import List
from enum import Enum

class Unit(Enum):
    # Metric unit for liquid ingredients
    ML = 1
    # Metric unit for solid ingredients
    GRAMS = 2
    # Non-metric units for adding other types of ingredients
    TEASPOONS = 3
    # Some non-specific amount, typically very small
    PINCH = 4


# TODO: Make these objects more JSON compatible -- this may require some
# annotations/modifiers
class IngredientQty:
    """
    Classify data about the quantity required of a certain ingredient and a
    simple name of the ingredient as well.
    """
    def __init__(self, name: str, qty: int, unit: Unit, cost: float) -> None:
        self._name = name
        self._unit = unit
        self._qty = qty
        self._cost = cost


class Recipe:
    """
    Data associated with a recipe
    """
    def __init__(self, recipe_name: str, ingredients_list: List[IngredientQty]) -> None:
        self._name = recipe_name
        self._ingredients_list = ingredients_list

    def add_ingredient(self, new_ingredient: IngredientQty) -> bool:
        """
        Add the ingredient to the current recipe ingredient list
        Returns False if there is already a duplicate entry in the ingredients
        list, not adding the ingredient
        Otherwise, returns True
        """
        if new_ingredient in self._ingredients_list:
            return False
        self._ingredients_list += [new_ingredient]
        return True
