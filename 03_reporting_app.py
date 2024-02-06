import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon = ":bar_chart:",
    layout="wide")
st.title("Sales Dashboard")
st.markdown("_Prototype v0.1_")

# @st.cache_data
# def load_data(path: str):
#     data = pd.read_excel(path)
#     return data

# df = load_data("./Financial Data Clean.xlsx")

@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

# upload file
with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file:")

# validate is a file uploaded
if uploaded_file is None:
    st.info("Upload a file through config")
    st.stop()
    
df = load_data(uploaded_file)

#show original data
with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={
            "Year" : st.column_config.NumberColumn(format="%d"),
        }
        )
    
all_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def plot_bottom_left():
    # unpivot for plotting
    sales_data = duckdb.sql(
        f"""
        WITH sales_data AS (
            SELECT
                Scenario, {','.join(all_months)}
            FROM df
                WHERE Year='2023'
                AND Account='Sales'
                AND business_unit='Software'
                )
        UNPIVOT sales_data
        ON {','.join(all_months)}
        INTO
            NAME month
            VALUE sales
        """
    ).df()
    #st.dataframe(sales_data)
    # st.line_chart(sales_data, x="month", y="sales")
    
    fig = px.line(
        sales_data,
        x="month",
        y="sales",
        color="Scenario",
        markers=True,
        text="sales",
        title="Monthly budget vs forecast 2023"
    )
    st.plotly_chart(fig, use_container_width=True) 
    
plot_bottom_left()