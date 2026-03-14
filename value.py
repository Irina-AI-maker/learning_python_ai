mission_participants = {'ирина': 'архитектор смыслов',
                      'Влад': 'кибернетика',
                      'Алиса': 'кибернетика',
                      'Боб': 'робототехника',}
print(f"В нашей лаборатории изучают:")
for mission in mission_participants.values():
    print(mission)

print(f"В нашей лаборатории изучают:")
for mission in set (mission_participants.values()):
    print(mission)