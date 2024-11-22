# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:30:06 2024

@author: jperezr
"""

import streamlit as st


# Configuración de la página de Streamlit debe ser la primera línea
st.set_page_config(page_title="Convocatoria - Coordinación para el Análisis de Economía Laboral en CONASAMI", layout="wide")


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título principal
st.title("Convocatoria para el Puesto de Coordinación para el Análisis de Economía Laboral en CONASAMI")

# Descripción de la convocatoria
st.write("""
    **¿Qué es CONASAMI?**
    
    La **Comisión Nacional de los Salarios Mínimos (CONASAMI)** es un órgano autónomo del gobierno mexicano encargado de regular los salarios mínimos en el país, garantizando que estos sean justos y adecuados para los trabajadores.
   
""")

# Agregar información adicional en la barra lateral
st.sidebar.header("Ayuda y Contacto")
st.sidebar.write("""
     
    **Desarrollado por:**
    - Javier Horacio Pérez Ricárdez
    - © 2024 Todos los derechos reservados.
""")
