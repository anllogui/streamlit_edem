import numpy as np
import pandas as pd
import streamlit as st 
from sklearn.linear_model import LinearRegression
import joblib 
import locale


model = joblib.load('model.pkl')

def format_euro(num):
    # Asegurarse de que num es un float si es un ndarray de un solo elemento
    if isinstance(num, np.ndarray):
        # Asumiendo que num es un ndarray de un solo elemento
        num = num.item()
        
    # Convertir el número a un string con dos decimales
    num_str = f"{num:.2f}"

    # Separar los decimales y los enteros
    parts = num_str.split('.')

    # Reemplazar el punto decimal por una coma
    decimal_part = parts[1].replace('.', ',')

    # Invertir la parte entera para facilitar la inserción de puntos cada tres dígitos
    integer_part_reversed = parts[0][::-1]

    # Insertar un punto cada tres dígitos
    formatted_integer_part = '.'.join([integer_part_reversed[i:i+3] for i in range(0, len(integer_part_reversed), 3)])

    # Reinvertir la parte entera formateada
    formatted_integer_part = formatted_integer_part[::-1]

    # Combinar las partes entera y decimal formateadas
    formatted_num = f"{formatted_integer_part},{decimal_part}€"

    return formatted_num

  
def main(): 
    st.title("Income Predictor")
    
    age = st.text_input("Experiencia","0") 
    
    if st.button("Predict"): 
               
        prediction = model.predict([[float(age)]])
        print(prediction)    
        output  = format_euro(prediction)

        st.success('Employee Income will be {}'.format(output))
      
if __name__=='__main__': 
    main()