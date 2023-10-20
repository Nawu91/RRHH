import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='App RRHH',
                    layout='wide')
   
st.title('Organigrama MDHYHGC')

with open("org.html", "r") as file:
    html_code = file.read()
components.html(html_code, width=1700, height=800, scrolling=True)