from collections import defaultdict

def solution(dishes):
  ingredient_to_dish = defaultdict(list)
  for dish in dishes:
    name = dish[0]
    ingredients = dish[1:]
    for i in ingredients:
      ingredient_to_dish[i].append(name)

  multi_ingredients = []
  for (k, v) in ingredient_to_dish.items():
    if len(v) > 1:
      multi_ingredients.append(k)
  multi_ingredients = sorted(multi_ingredients)
  # multi_ingredients = sorted(filter(lambda k,v: len(v) > 1, ingredient_to_dish.items()))
  
  by_ingredients = []
  for m in multi_ingredients:
    sorted_dishes = sorted(ingredient_to_dish[m])
    by_ingredients.append([m] + sorted_dishes)
    
  # print(by_ingredients)
  return by_ingredient
