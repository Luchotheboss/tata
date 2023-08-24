# tata
import streamlit as st
from PIL import image

st.title("Mi primera app")

st.header("Aplicaciones")
st.write("Backend y frontend")
image = Image.open('png-transparent-cat-kitty-creative-cat-cat')

st.image(image, caption= 'Interfaces multimodales')
