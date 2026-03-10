import streamlit as st
discovered_concepts=["нейроны","алгоритмы","логика","данные","веса"]
st.write(f"Список в алфавитном порядке:{discovered_concepts}")
st.write(f"Список в алфавитном порядке (временно):{",".join(sorted(discovered_concepts))}")
st.write(f"Оригинальный список всё еще такой: {','.join(discovered_concepts)}")
st.write(f"В списке находятся: первое - {discovered_concepts[0]}, второе - {discovered_concepts[1]}, третье - {discovered_concepts[2]}, четвертое - {discovered_concepts[3]}. ")
st.write(f"Список в обратном порядке: {list(reversed(discovered_concepts))}")
 