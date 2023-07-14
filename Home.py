import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image

st.set_page_config(page_title='App RRHH',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")
   
st.title('Gerencia Operativa Gestión de Recursos Humanos')
background_image_path = ("BA.jpg")
background_image = Image.open(background_image_path)
st.image(background_image, use_column_width=True)