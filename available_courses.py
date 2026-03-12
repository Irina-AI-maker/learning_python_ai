available_courses = ['параллельные вычисления', "линейная алгебра", 'статистика', 'интерфейсы многоядерных систем']
requested_courses = ['параллельные вычисления', "линейная алгебра", 'высшая математика']
for requested_course in requested_courses:
    if requested_course in available_courses:
        print(f"Ваш требуемый курс {requested_course} есть в наличии")
    else:
        print(f"Извините, но курса {requested_course} нет в наличии в данный момент" )
print("\n Спасибо за обращение!")