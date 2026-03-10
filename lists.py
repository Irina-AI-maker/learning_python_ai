import streamlit as st
ai_goals=["нейросети","алгоритмы","данные"]
message=(f"Фундамент ИИ - это {ai_goals[-1].upper()}")
st.write(message)
ai_goals[-1]="Big Data"
message=(f"Фундамент ИИ — это {ai_goals[-1].upper()}")
st.write(message)
ai_goals.append("python")
message=(ai_goals)
st.write(message)
