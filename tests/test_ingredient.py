import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.get_price() == 100

def test_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    assert ingredient.get_name() == "cutlet"

def test_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150)
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE