import streamlit as st
import time

## FORMATS
st.title("Bienvenido a Streamlit", anchor="title")
st.write("bajo del título")

st.header("Esto es un header", anchor="chap-1")
st.write("Bajo del header")

st.header("Esto es otro header", anchor="chap-2")
st.write("bajo del otro header")

st.subheader("esto es un subheader")
st.write("esto debajo del subheader")

st.markdown("# Bienvenido a Streamlit")

## DISTRIBUTIONS

col1, col2, col3 = st.columns([1,3,2])
col1.markdown("Esto es un texto normal en col1")
col2.markdown("Esto es un texto normal en col2")
col3.markdown("Esto es un texto normal en col3")

with col2:
    col21, col22, col23 = st.columns([1,1,1])

    col21.markdown("subcol21")
    col22.markdown("subcol22")
    col23.markdown("subcol23")


## IMAGES
uploaded_photo = st.file_uploader("Sube una foto")
camera_photo = st.camera_input("Toma una foto con la cámara")

## PROGRESS
progress_bar = st.progress(0)

# for percentage in range(100):
#     time.sleep(0.05)
#     progress_bar.progress(percentage+1)

st.success("Subida foto correctamente!")

## METRICS
st.metric(label="Temperatura", value="60 ºC", delta="-3 ºC")

## EXPANDER
with st.expander("Pincha aquí para expandir"):
    st.write("Esta es la información que estaba oculta dentro del expander")

    if uploaded_photo is None:
        if camera_photo is None:
            st.write("Sube una foto por favor.")
            st.stop()
        else:
            st.image(camera_photo)
    else:
        st.image(uploaded_photo)
