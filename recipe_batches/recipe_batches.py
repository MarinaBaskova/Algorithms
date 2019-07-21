#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  compared_values =[]
  if(recipe.keys() == ingredients.keys()):
    for key, value in ingredients.items(): 
        compared_values.append(value/ recipe[key])
    number_of_dishes = min(compared_values)     
  else:
    return 0  

  return  math.floor(number_of_dishes) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))