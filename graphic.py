import pandas as pd
import plotly.express as px
import plotly.offline as offline
import plotly.graph_objects as go


# Функция для построения графика
def construct_graphic(coor_x: list[int | float | str], coor_y: list[int | float]):
    
    """Функция принимает на вход два списка и по ним строит график.

    Args:
        coor_x (list[int | float | str]): Список координат x (Например, h - время)
        coor_y (list[int | float]): Список координат y (Например, t - температура)
    """
    
    const_color_1 = "#8A2BE2"  # Основной цвет
    const_color_2 = "#EE82EE"  # Цвет для "предсказания"

    fig = go.Figure()

    # Добавляем основной трейс для первых отрезков линии
    fig.add_trace(go.Scatter(
        x=coor_x[:-3],  # Все, кроме последних трех x
        y=coor_y[:-3],  # Все, кроме последних трех y
        mode='lines+markers',
        marker=dict(size=8, color=const_color_1),
        line=dict(color=const_color_1),
        name='Основной',
        showlegend=False
    ))

    # Добавляем трейс для отрезка от 5ой до 6ой точки
    fig.add_trace(go.Scatter(
        x=coor_x[-4:-2],
        y=coor_y[-4:-2],
        mode='lines+markers',
        marker=dict(size=8, color=const_color_2),
        line=dict(color=const_color_2),
        name='Предсказание',
        showlegend=False
    ))

    # Добавляем трейс для отрезка от 6ой до 7ой точки
    fig.add_trace(go.Scatter(
        x=coor_x[-3:-1],
        y=coor_y[-3:-1],
        mode='lines+markers',
        marker=dict(size=8, color=const_color_2),
        line=dict(color=const_color_2),
        name='Предсказание',
        showlegend=False
    ))

        # Добавляем трейс для отрезка от 7ой до 8ой точки
    fig.add_trace(go.Scatter(
        x=coor_x[-3:],
        y=coor_y[-3:],
        mode='lines+markers',
        marker=dict(size=8, color=const_color_2),
        line=dict(color=const_color_2),
        name='Предсказание',
        showlegend=False
    ))

    # Обновляем макет графика
    fig.update_layout(
        title='График погоды',
        xaxis_title='Время',
        yaxis_title='Температура',
        font=dict(
            family="Courier New, monospace",
            size=20,
            color="#00BFFF"
        ),
        template='plotly_dark',
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=False  
    )

    offline.plot(fig, filename='graphic_html.html', auto_open=False, include_plotlyjs='cdn')
    
 # Тестовые данные   
test_x = ['5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00']
test_y = [-6, -4, -2, 0, 1, 3, 5, 7]

construct_graphic(coor_x=test_x, coor_y=test_y) 
    