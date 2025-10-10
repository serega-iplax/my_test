from main import get_data, from_data_to_dataframe
import streamlit as st
import pandas as pd


### ---
city = "Москва"
data_dict = get_data(city)
df = from_data_to_dataframe(data_dict)
st.title("График погоды v2")


if not df.empty:
    st.line_chart(df.set_index('dates')['temperatures'])
else:
    st.write("Нет данных для отображения.")    
