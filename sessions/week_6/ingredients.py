def read_ingredients(file_name):
    ingredients_dict = {}
    with open(file_name) as ingredients_file:
        for line in ingredients_file:
            line = line.replace("\n", "")
            name, kcal, protein, fat = line.split(",")
            ingredients_dict[name] = (kcal, protein, fat)
    return ingredients_dict


def save_ingredients(file_name, ingredients_dict):
    with open(file_name, "w") as ingredients_file:
        for ingredient in ingredients_dict:
            kcal, protein, fat = ingredients_dict[ingredient]
            ingredients_file.write("{},{},{},{}\n".format(ingredient, kcal, protein, fat))


if __name__ == '__main__':
    ingredients = read_ingredients("information.csv")

    # ask user for additional ingredients

    save_ingredients("ingredients.csv", ingredients)
