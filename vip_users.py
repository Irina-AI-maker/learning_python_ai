import streamlit as st

st.title("Система контроля доступа")

# 1. Создаем "Белый список"
vip_users = ['irina', 'vlad', 'sonya', 'bob']

# 2. Получаем имя от пользователя (убираем лишние пробелы и приводим к нижнему регистру для точности)
current_user = st.text_input("Введите ваше имя:").lower().strip()

# 3. Проверяем логику, только если пользователь что-то ввел
if current_user:
    if current_user in vip_users:
        st.success(f"Добро пожаловать в систему, {current_user.title()}! ✅")
    else:
        st.error(f"{current_user.title()}, доступ ограничен. Обратитесь к администратору. 🛑")