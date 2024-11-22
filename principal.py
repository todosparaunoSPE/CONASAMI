# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:30:06 2024

@author: jperezr
"""

import streamlit as st

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


import streamlit as st

# Configuración de la página de Streamlit debe ser la primera línea
st.set_page_config(page_title="Convocatoria - Coordinación para el Análisis de Economía Laboral en CONASAMI", layout="wide")

# Título principal
st.title("Convocatoria para el Puesto de Coordinación para el Análisis de Economía Laboral en CONASAMI")

# Descripción de la convocatoria
st.write("""
    **¿Qué es CONASAMI?**
    
    La **Comisión Nacional de los Salarios Mínimos (CONASAMI)** es un órgano autónomo del gobierno mexicano encargado de regular los salarios mínimos en el país, garantizando que estos sean justos y adecuados para los trabajadores.

    **Objetivo del Puesto:**
    
    El puesto de **Coordinación para el Análisis de Economía Laboral** tiene como principal objetivo realizar estudios y análisis sobre la evolución del mercado laboral, los salarios mínimos, las condiciones económicas y su impacto en los trabajadores a nivel nacional.

    **Responsabilidades Principales:**
    
    - Analizar las tendencias del mercado laboral en México.
    - Evaluar el impacto de las políticas públicas sobre los salarios mínimos y la economía laboral.
    - Colaborar con otros departamentos para la elaboración de estudios y recomendaciones.
    - Preparar reportes y presentaciones con datos relevantes para las decisiones de CONASAMI.

    **Requisitos del Puesto:**
    
    - Título universitario en Economía, Ciencias Sociales, Administración Pública o áreas afines.
    - Experiencia previa en análisis económico y laboral.
    - Conocimiento en la interpretación de datos estadísticos y económicos.
    - Habilidades de comunicación y presentación de informes.

    **¿Cómo Postularse?**
    
    Los interesados deben enviar su CV actualizado y una carta de motivación a la dirección de CONASAMI antes del **[fecha límite]**.
    
    Para más información, consulta la página oficial de **CONASAMI** o contacta a [email de contacto].
""")

# Agregar información adicional en la barra lateral
st.sidebar.header("Ayuda y Contacto")
st.sidebar.write("""
    Para más detalles sobre el proceso de selección y el puesto, visita la página oficial de CONASAMI o envía un correo electrónico a la dirección proporcionada.
    
    **Desarrollado por:**
    - Javier Horacio Pérez Ricárdez
    - © 2024 Todos los derechos reservados.
""")
