import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title='Cuadro de Mandos Complejo', layout='wide')

# Cargar datos de Excel
@st.cache
def cargar_datos(ruta_excel):
    df = pd.read_excel(ruta_excel)
    return df

# Crear la barra lateral con la carga del archivo Excel
st.sidebar.header('Carga de Datos')
archivo_excel = st.sidebar.file_uploader('Sube tu archivo Excel', type=['xlsx'])

# Verificar si se ha cargado un archivo
if archivo_excel is not None:
    df = cargar_datos(archivo_excel)
    st.sidebar.success('Datos cargados correctamente!')

    # Mostrar los datos crudos en la aplicación
    if st.sidebar.checkbox('Mostrar datos crudos'):
        st.subheader('Datos Crudos')
        st.write(df)

    # Crear cuadro de mandos si hay datos
    if df is not None:
        # Selección de columnas para análisis
        columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()
        columnas_categoricas = df.select_dtypes(exclude=np.number).columns.tolist()

                # Sección de estadísticas descriptivas
        if st.sidebar.checkbox('Mostrar estadísticas descriptivas'):
            st.subheader('Estadísticas Descriptivas')
            st.write(df.describe())

        # Sección de gráficos
        st.sidebar.subheader('Visualización de Datos')

                # Selección de tipo de gráfico
        tipo_grafico = st.sidebar.selectbox('Selecciona el tipo de gráfico',
                                            ('Histograma', 'Boxplot', 'Barras', 'Lineas', 'Correlaciones'))

                # Configuración de gráficos según el tipo elegido
        if tipo_grafico == 'Histograma':
            st.subheader('Histograma')
            columna_hist = st.sidebar.selectbox('Selecciona la columna para el histograma', columnas_numericas)
            bins = st.sidebar.slider('Número de bins', min_value=5, max_value=100, value=20)
            fig, ax = plt.subplots()
            ax.hist(df[columna_hist], bins=bins)
            st.pyplot(fig)

        elif tipo_grafico == 'Boxplot':
            st.subheader('Boxplot')
            columna_box = st.sidebar.selectbox('Selecciona la columna para el boxplot', columnas_numericas)
            fig, ax = plt.subplots()
            sns.boxplot(data=df[columna_box], ax=ax)
            st.pyplot(fig)

        elif tipo_grafico == 'Barras':
            st.subheader('Gráfico de Barras')
            columna_bar_x = st.sidebar.selectbox('Selecciona la columna para el eje X', columnas_categoricas)
            columna_bar_y = st.sidebar.selectbox('Selecciona la columna para el eje Y', columnas_numericas)
            fig, ax = plt.subplots()
            sns.barplot(x=columna_bar_x, y=columna_bar_y, data=df, ax=ax)
            st.pyplot(fig)

        elif tipo_grafico == 'Lineas':
            st.subheader('Gráfico de Líneas')
            columna_line_x = st.sidebar.selectbox('Selecciona la columna para el eje X', columnas_numericas)
            columna_line_y = st.sidebar.selectbox('Selecciona la columna para el eje Y', columnas_numericas)
            fig, ax = plt.subplots()
            sns.lineplot(x=columna_line_x, y=columna_line_y, data=df, ax=ax)
            st.pyplot(fig)

        elif tipo_grafico == 'Correlaciones':
            st.subheader('Mapa de Calor de Correlaciones')
            fig, ax = plt.subplots()
            sns.heatmap(df[columnas_numericas].corr(), annot=True, fmt=".2f", ax=ax)
            st.pyplot(fig)

else:
    st.info('Esperando a que se cargue un archivo Excel...')
