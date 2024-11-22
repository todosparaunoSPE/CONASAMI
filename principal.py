# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:30:06 2024

@author: jperezr
"""

import streamlit as st

# Configuración de la página de Streamlit
st.set_page_config(page_title="Convocatoria - Coordinación para el Análisis de Economía Laboral en CONASAMI", layout="wide")

# Título principal
st.title("Convocatoria para el Puesto de Coordinación para el Análisis de Economía Laboral en CONASAMI")



# Agregar información adicional en la barra lateral
st.sidebar.header("Ayuda y Contacto")
st.sidebar.write("""
       
    **Desarrollado por:**
    - Javier Horacio Pérez Ricárdez
    - © 2024 Todos los derechos reservados.
""")