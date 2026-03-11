import streamlit as st
st.title("Система контроля доступа ИИ")
# Получаем данные от "пользователя"
age = st.number_input("Ваш возраст:", min_value=0, max_value=100, value=20)
level = st.number_input("Уровень допуска (1-10):", min_value=1, max_value=10, value=5)

if st.button("Запросить доступ"):
    if age >= 18 and level > 5:
        st.success("Доступ в секретную лабораторию разрешен! 🔓")
    elif age < 18:
        st.error("Доступ запрещен: слишком юный возраст. 🛑")
    else:
        st.warning("Недостаточный уровень допуска. Обратитесь к администратору. ⚠️")

