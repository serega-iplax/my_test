from main import get_data, from_data_to_dataframe
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


city = "Москва"
data_dict = get_data(city)
df = from_data_to_dataframe(data_dict)
df = df.sort_values("date")
st.title("График :)")


if not df.empty:
    
    # Последние 3 точки
    last_points = df[-3:]

    fig = go.Figure()

    # Вся линия синяя
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['temperature'],
        mode='lines',
        line=dict(color="#1F2972"),
        name="Основная линия"
    ))

    # Точки везде, где есть данные, синие
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['temperature'],
        mode='markers',
        marker=dict(color="#1F2972", size=8),
    ))

    # Линия, соединяющая последние 3 точки, красная
    fig.add_trace(go.Scatter(
        x=last_points['date'],
        y=last_points['temperature'],
        mode='lines',
        line=dict(color='red', width=2),
        name="Предсказание нейросети"
    ))

    # Точки последних 3 значений красным цветом
    fig.add_trace(go.Scatter(
        x=last_points['date'],
        y=last_points['temperature'],
        mode='markers',
        marker=dict(color="red", size=10),
    ))
    
    # Настройка осей
    fig.update_layout(
        xaxis=dict(
            tickformat='%d.%m %H:%M',  
            tickmode='auto',
            dtick=3600*3*1000,  
            ticklabelmode='instant',
            tickangle=45  
        ),
        yaxis=dict(
            tick0=0,  
            dtick=1,  
            title='Температура, °C'
        ),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.write("Нет данных для отображения.")
    