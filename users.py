users = ['irina','alise', 'vlad','john','nadya',]
for user in users:
    if user == 'irina':
        print(f"{user.upper()} - админ чата")
    elif user == 'vlad':
        print(f"{user.title()} - помощник админа")
    else:
        print(f"{user.title()} - пользователь")
print("Добро пожаловать в чат")