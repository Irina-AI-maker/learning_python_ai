available_modules = ['нейросеть', 'логика', 'интерфейс']
requested_modules = ['нейросеть', 'камера', 'логика']

if requested_modules: # Проверяем, не пуст ли список запросов
    for module in requested_modules:
        if module in available_modules:
            # Вложенная проверка на "особенность"
            if module == 'нейросеть':
                print("Загрузка ТЯЖЕЛОГО модуля 'нейросеть'... подождите.")
            else:
                print(f"Загружаю модуль: {module.title()}.")
        else:
            print(f"Ошибка: модуля '{module}' нет в системе!")
else:
    print("Вы не выбрали ни одного модуля.")