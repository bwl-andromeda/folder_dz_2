from pprint import pprint
with open('recipe.txt', encoding="UTF-8") as file:
    cook_book = {}
    for line in file:
        dish_names = line.strip()
        count_ingridients = int(file.readline())
        ingridients_1 = []
        for _ in range(count_ingridients):
            Ingredients = file.readline().strip()
            ingredient_name,quantity,measure = Ingredients.split(" | ")
            ingridients_1.append(
                {"ingredient_name": ingredient_name ,"quantity": quantity , "measure": measure}
                                  )
        cook_book[dish_names] = ingridients_1
        file.readline()

# pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    list_1 = []
    list_2 = []
    list_3 = []
    for i in cook_book.keys():
        # print(i)
        for j in dishes:
            # print(j)
            if i == j:
                list_1 += cook_book[i]
    for id in list_1:
        for key,value in list(id.items()):
            if key == "ingredient_name":
                list_2.append(value)
    for id in list_1:
        list_3.append({"measure": id["measure"], "quantity": int(id["quantity"])*person_count})
    
    for id in zip(list_2,list_3):
        print(id)
    #zip,затирается всё если dict , 2 словаря (1 - все уникальные , 2 - всё ) ,  совпадали значения ключей , то складывал по values ... 
    # print(list_2)
    # print(list_3)
            

get_shop_list_by_dishes(["Омлет","Жаренная картошка","Запеченный картофель"],2)
