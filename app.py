# tata
import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("Aplicaciones")
st.write("Backend y frontend")
image = Image.open('gatico.png')

st.image(image, caption= 'Interfaces multimodales')
