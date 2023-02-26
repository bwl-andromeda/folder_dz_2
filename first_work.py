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

# pprint(cook_book,width=100)

def get_shop_list_by_dishes(dishes, person_count):
    list_1,list_2,list_3 = [],[],[] 
    for i in cook_book.keys():
        for j in dishes:
            if i == j:
                list_1 += cook_book[i]
    for id in list_1:
        for key,value in list(id.items()):
            if key == "ingredient_name":
                list_2.append(value)
    for id in list_1:
        list_3.append({"measure": id["measure"], "quantity": int(id["quantity"])*person_count})
        
    zipped = list(zip(list_2,list_3))
    basic_dict = {}
    future_dict = {}
    for i,j in zipped:
        if i not in basic_dict.keys():
            basic_dict[i] = j
        else:
            future_dict[i] = j
    for a,b in basic_dict.items():
        for c,d in future_dict.items():
            if a == c:
                b["quantity"]+=d["quantity"]
    pprint(basic_dict)



get_shop_list_by_dishes(["Омлет","Жаренная картошка","Запеченный картофель"],2)
