def cakes(recipe, available):
    result = []
    for key_in_recipe in recipe:
        if key_in_recipe in available:
            result.append(available[key_in_recipe] // recipe[key_in_recipe])
        else:
            return 0
    return min(result)


print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1500, "sugar": 1200, "eggs": 5, "milk": 200}))
