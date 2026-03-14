mission_participants = {'ирина': 'архитектор смыслов',
                      'Влад': 'кибернетика',
                      'Алиса': 'Нейросети',
                      'Боб': 'робототехника',}


friends = ['ирина', 'Влад', 'соня']
for name in mission_participants.keys():
    print(f"Привет {name.title()}!")

    if name in friends:
        friend_mission = mission_participants[name].title()
        print(f"Рад тебя видеть, {name.title()}! Твоя миссия — {friend_mission}.")


