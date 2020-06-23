# imports
import pandas as pd
import datetime as dt

# class definitions



class Recipe:

    def updatetotaltime(self):
        self.total = self.prep_time + self.cook_time

    def __init__(self, name, servings, prep_time, cook_time, ingredients, instructions, equipment):
        self.name = name
        self.servings = servings
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.ingredients = ingredients
        self.instructions = instructions
        self.equipment = equipment

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.instructions)

    def __iter__(self):
        return iter(self.ingredients)

    def __next__(self):
        return next(self.ingredients)

class RecipeBook:
    
    def __init__(self, name, *args):
        self.name = name
        self.recipes = []
        for recipe in args:
            self.recipes.append(recipe)

    def __repr__(self):
        return self.name

    


# function definitions



# script

chilligarlicspag = Recipe('Chilli, Garlic Spaghetti', 1, 3.0, 12.0, [{'Name': 'Wholemeal spaghetti', 'Amount': 75, 'Unit': 'g'}, {'Name': 'Olive Oil', 'Amount': 1, 'Unit': 'tbsp'}, {'Name': 'Chilli Flakes', 'Amount': 0.5, 'Unit': 'tsp'}, {'Name': 'Garlic', 'Amount': 1, 'Unit': 'clove'}, {'Name': 'Rocket', 'Amount': 1, 'Unit': 'handful'}], [{'Index': 1, 'Method': 'Cook the pasta according to instructions.'}, {'Index': 2, 'Method': 'Put the olive oil in a small frying pan and add the chilli and garlic, cook for 1 minute.'}, {'Index': 3, 'Method': 'Drain the pasta and add to the frying pan, mix so all the pasta is coated.'}, {'Index': 4, 'Method': 'Garnish with the rocket on top.'}], ['Saucepan', 'Frying Pan', 'Sieve'])

print(chilligarlicspag)
print(type(chilligarlicspag))
print(len(chilligarlicspag))

for x in chilligarlicspag:
    print(x)

print(chilligarlicspag.prep_time)
print(chilligarlicspag.cook_time)

print(chilligarlicspag.prep_time + chilligarlicspag.cook_time)