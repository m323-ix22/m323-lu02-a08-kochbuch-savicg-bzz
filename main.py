"""
Aufgabe:
"""
import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipe_, num_people):
    factor = num_people / recipe_['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe_['ingredients'].items()}
    adjusted_recipe_ = recipe_.copy()
    adjusted_recipe_['ingredients'] = adjusted_ingredients
    adjusted_recipe_['servings'] = num_people
    return adjusted_recipe_


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(recipe, 2)
    print(json.dumps(adjusted_recipe, indent=4))
