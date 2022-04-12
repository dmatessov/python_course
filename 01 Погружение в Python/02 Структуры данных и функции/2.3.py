recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}

def reduce_store(tmp_store, recip):
    try:
        for ingredient in recip:
            new_value = tmp_store[ingredient] - recip[ingredient]
            if new_value >= 0:
                tmp_store[ingredient] = new_value
            else:
                raise Exception
                break
        return True
    except Exception:
        return False


def check_portions(food, count, recipes=recipes, store=store):
    recip = recipes.get(food)
    response_code = 0
    av_count = 0
    if recip is not None:
        tmp_store = store.copy()
        while av_count < count:
            # Проверка доступности

            if reduce_store(tmp_store, recip):
                av_count += 1
            else:
                break
    if av_count == count:
        response_code = 1
    return tuple((response_code, av_count))