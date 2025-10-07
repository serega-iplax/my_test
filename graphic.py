import plotly.offline as offline
import plotly.graph_objects as go



# Функция для построения графика
def construct_graphic(coor_x: list[int | float | str], coor_y: list[int | float]):

    """Функция принимает на вход два списка и по ним строит график.

    Args:
        coor_x (list[int | float | str]): Список координат x (Например, h - время)
        coor_y (list[int | float]): Список координат y (Например, t - температура)
    """

    const_color_1 = "#00FFFF"  # Основной цвет 
    const_color_2 = "#7DF9FF"  # Цвет для "предсказания" 

    fig = go.Figure()

    # Основной трейс для первых отрезков линии
    fig.add_trace(go.Scatter(
        x=coor_x[:-3],  # Все, кроме последних трех x
        y=coor_y[:-3],  # Все, кроме последних трех y
        mode='lines+markers',
        marker=dict(size=8, color=const_color_1, line=dict(width=2, color='white')),  
        line=dict(color=const_color_1, width=3),  
        name='Основной',
        showlegend=False
    ))

    # Дополнительный трейс для "предсказания" (Последние 3 промежутка)
    fig.add_trace(go.Scatter(
        x=coor_x[-4:],  # Последние 4 точки
        y=coor_y[-4:],  # Последние 4 точки
        mode='lines+markers',
        marker=dict(size=8, color=const_color_2, line=dict(width=2, color='white')),  
        line=dict(color=const_color_2, width=3, dash='dash'),  
        name='Предсказание',
        showlegend=False
    ))

    
    fig.update_layout( 
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
test_x = ["15.10.25", "16.10.25", "17.10.25", "18.10.25", "19.10.25"]
test_y = ["9°C", "7°C", "8°C", "8°C", "6°C"]

construct_graphic(coor_x=test_x, coor_y=test_y) 
    