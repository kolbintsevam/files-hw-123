# Задание № 1
cook_book = {}
with open('file1.txt', 'rt', encoding='utf8') as file:
        for d in file:
            dish = d.strip()
            cook_book[dish] = []
            ingridients_count = file.readline()
            for ingridient in range(int(ingridients_count)):
                ing = file.readline()
                ingridient_name, quantity, measure = ing.split(' | ')
                ingridients_list = {'ingridient_name': ingridient_name, 'quantity': quantity,
                                    'measure': measure.strip()}
                cook_book[dish].append(ingridients_list)
            blank_line = file.readline()

#Задание № 2 не смогла найти ошибку, помогите, пжл, код не срабатывает
def get_shop_list_by_dishes(dishes, person_count):
    dic = {}
    for dish in dishes:
        for ings in cook_book[dish]:
            if ings["ingredient_name"] in dic.keys():
                dic[ings["ingredient_name"]]["quantity"] = str(int(dic[ings["ingredient_name"]]["quantity"]) * person_count)
            else:
                dic[ings["ingredient_name"]] = {"measure": ings["measure"], "quantity": str(int(ings["quantity"]) * person_count)}
    return dic

print(cook_book)
print()
print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))

