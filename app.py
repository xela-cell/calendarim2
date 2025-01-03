{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang3082{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang10 import pandas as pd\par
import streamlit as st\par
\par
# Cargar los datos procesados\par
data = pd.DataFrame(\{\par
    'Fecha': ['2024-10-27', '2024-11-01', '2024-11-08', '2024-11-09', '2024-11-09'],\par
    'Local': ['OBV IM2 GEA ASESORES', 'OBV IM2 GEA ASESORES', 'OBV IM2 GEA ASESORES', 'BERJA IMB', 'BERJA IMA'],\par
    'Visitante': ['ECONORIAS AL-BAYYANA IM', 'Cajamar MINTONETTE ALMER\'cdA ROSA IM', 'Cajamar MINTONETTE ALMER\'cdA BLANCO IM', 'OBV IM2 GEA ASESORES', 'OBV IM2 GEA ASESORES'],\par
    'Lugar': ['ANEXA A', 'CENTRAL 2', 'CENTRAL 2', 'BERJA 1', 'BERJA 2'],\par
    'Hora': ['12:30:00', '18:30:00', '18:30:00', '09:30:00', '13:00:00']\par
\})\par
\par
data['Fecha'] = pd.to_datetime(data['Fecha'])\par
\par
# T\'edtulo de la app\par
st.title("Calendario de Partidos")\par
\par
# Filtrar por nombre de equipo\par
team_filter = st.text_input("Buscar equipo (Local o Visitante):")\par
if team_filter:\par
    data = data[data['Local'].str.contains(team_filter, case=False) | data['Visitante'].str.contains(team_filter, case=False)]\par
\par
# Filtrar por rango de fechas\par
st.sidebar.header("Filtrar por Fecha")\par
start_date = st.sidebar.date_input("Fecha de inicio", data['Fecha'].min().date())\par
end_date = st.sidebar.date_input("Fecha de fin", data['Fecha'].max().date())\par
\par
if start_date and end_date:\par
    data = data[(data['Fecha'] >= pd.to_datetime(start_date)) & (data['Fecha'] <= pd.to_datetime(end_date))]\par
\par
}
 