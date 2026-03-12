modules = []

for module in modules:       
    if module == 'нейросеть':
        print("Загрузка тяжелого модуля 'нейросеть'... подождите.")
    else: # Тот же отступ, что у if!
        print(f"Модуль {module} загружен.")