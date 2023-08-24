# tata
import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("Aplicaciones")
st.write("Backend y frontend")
image = Image.open('gatico.png')

st.image(image, caption= 'Interfaces multimodales')

st.header("2 columnas")

col1, col2 = st.colums(2)

with col1:
  st.subheader("Primera columna")
  st.write("las interfaces multimodales mejoran la experiencia")
  resp = st,checkbox('estoy de acuerdo')
  if resp:
    st.write('Correctol')
