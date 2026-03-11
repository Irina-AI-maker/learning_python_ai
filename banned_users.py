import streamlit as st


st.title("Система контроля доступа")

# 1. Создаем "Черный  список"
banned_users = ['vlad_hasker', 'sonya_spammer', 'bob']

# 2. Получаем имя от пользователя (убираем лишние пробелы и приводим к нижнему регистру для точности)
current_user = st.text_input("Введите ваш логин:")

# 3. Проверяем логику, только если пользователь что-то ввел
if current_user:
    if current_user not in banned_users:
        st.info(f"Ваш аккаунт прошел проверку безопасности! ✅")
    else:
        st.error(f"{current_user.title()}, доступ ограничен. Обратитесь к администратору. 🛑")