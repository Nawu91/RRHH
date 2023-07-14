import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='Dotacion RRHH',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")

    
@st.cache_data
def get_data():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)
df_anual = get_data()
st.title('Tablero de indicadores DGDIM-RRHH _ Dotaciones')
st.header('Dotacion Mensual')
st.divider() 
periodos = df_anual['Periodo']
lista_periodo = periodos.unique().tolist()
lista_items_ordenada = sorted(lista_periodo)
selected_periodo = st.selectbox('Selecciona el periodo',lista_items_ordenada)
df= df_anual[df_anual['Periodo'] == selected_periodo]
df_count = df_anual.groupby(['Periodo', 'Modalidad']).size().reset_index(name='Count')
df_graf= df.groupby(['Reparticion General', 'Modalidad']).size().reset_index(name='Contador')

ausup = df[(df["Modalidad"] == "Autoridades Superiores")]["Modalidad"].count()
cg = df[(df["Modalidad"] == "Carrera Gerencial")]["Modalidad"].count()
gab = df[(df["Modalidad"] == "Gabinete")]["Modalidad"].count()
pp = df[(df["Modalidad"] == "Planta Permanente")]["Modalidad"].count()
pt = df[(df["Modalidad"] == "Plantas Transitorias")]["Modalidad"].count()
conls = df[(df["Modalidad"] == "CLS")]["Modalidad"].count()
at = df[(df["Modalidad"] == "AT")]["Modalidad"].count()

ausup_ta = df[(df["Modalidad"] == "Autoridades Superiores")]["Total Asig"].sum()
cg_ta = df[(df["Modalidad"] == "Carrera Gerencial")]["Total Asig"].sum()
gab_ta = df[(df["Modalidad"] == "Gabinete")]["Total Asig"].sum()
pp_ta = df[(df["Modalidad"] == "Planta Permanente")]["Total Asig"].sum()
pt_ta = df[(df["Modalidad"] == "Plantas Transitorias")]["Total Asig"].sum()
conls_ta = df[(df["Modalidad"] == "CLS")]["Total Asig"].sum()
at_ta = df[(df["Modalidad"] == "AT")]["Total Asig"].sum()

ind1, ind2, ind3, ind4, ind5, ind6, ind7 = st.columns(7)

ind1.metric(label='Autoridades Superiores',
                value=int(ausup),
                delta='$' + format(ausup_ta,'0,.2f'),
                delta_color="normal",)
ind2.metric(label='Carreras Gerenciales',
                value=int(cg),
                delta='$' + format(cg_ta,'0,.2f'),
                delta_color="normal",)
ind3.metric(label='Gabinetes',
                value=int(gab),
                delta='$' + format(gab_ta,'0,.2f'),
                delta_color="normal",)
ind4.metric(label='Plantas Permanentes',
                value=int(pp),
                delta='$' + format(pp_ta,'0,.2f'),
                delta_color="normal",)
ind5.metric(label='Plantas Transitorias',
                value=int(pt),
                delta='$' + format(pt_ta,'0,.2f'),
                delta_color="normal",)
ind6.metric(label='CLS',
                value=int(conls),
                delta='$' + format(conls_ta,'0,.2f'),
                delta_color="normal",)
ind7.metric(label='AT',
                value=int(at),
                delta='$' + format(at_ta,'0,.2f'),
                delta_color='normal',)

areas = px.bar(data_frame= df_graf,
                x='Reparticion General',
                y='Contador',
                color="Modalidad",
                barmode='relative',
                title = 'Reparticiones mensual',
                color_discrete_sequence=px.colors.qualitative.Set2,
                width=1450,
                height=700,
                text_auto=True)
areas.update_traces(textposition='outside')
sorted_df = df_graf.sort_values('Contador', ascending=False)
x_sorted = sorted_df['Reparticion General']
areas.update_layout(
    xaxis={'categoryorder': 'array', 'categoryarray': x_sorted})

st.plotly_chart(areas,theme="streamlit", use_conatiner_width=True)
st.divider() 
st.header('Anual 2023')

lineas = px.bar(df_count, 
                x="Periodo",
                y='Count', 
                color='Modalidad',
                barmode='group',
                title = 'Modalidades por año',
                width=1450,
                height=400,
                color_discrete_sequence=px.colors.qualitative.Set2,
                text_auto=True)
st.plotly_chart(lineas,theme="streamlit", use_conatiner_width=True)

df_anual_totales = df_anual.groupby(['Periodo']).size().reset_index(name='Count')
lineas_anuales = px.line(df_anual_totales,
                x='Periodo',
                y='Count',
                width=1200,
                height=400,
                title = 'Total anual',
                range_y = (4000,5000),
                line_shape= 'linear',
                text='Count',
                color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(lineas_anuales,theme="streamlit", use_conatiner_width=True)