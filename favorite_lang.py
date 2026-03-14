favorite_languages = {'ирина': 'архитектор смыслов',
                      'Влад': 'кибернетика',
                      'Алиса': 'Нейросети',
                      'Боб': 'робототехника',}
print(f"Миссия Ирины {favorite_languages['ирина'].title()}")
mission = favorite_languages.get("Саша", "Миссия этого участника пока не определена.")
print(mission)