import pandas as pd
import plotly.express as px
import plotly.offline as offline


# Функция для построения графика
def construct_graphic(coor_x: list[int | float | str], coor_y: list[int | float]):
    
    """Функция принимает на вход два списка и по ним строит график.

    Args:
        coor_x (list[int | float | str]): Список координат x (Например, h - время)
        coor_y (list[int | float]): Список координат y (Например, t - температура)
    """
    
    const_color_1 = "#8A2BE2" # Для основных линий
    const_color_2 = "#EE82EE" # Для нейросети (предсказывание погоды) 
    segment = [const_color_1 for _ in range(len(coor_x) - 3)] + [const_color_2, const_color_2, const_color_2]
    data = {
        'x': coor_x,
        'y': coor_y,
        'segment': segment
    }
    df = pd.DataFrame(data) # Данные для график х, у, цвета для определенных линий
    fig = px.line(
        df,
        x='x',
        y='y',  
        title='График погоды',
        markers=True,
        labels={'x': 'Время', 'y': 'Температура'},
        template='plotly_dark',
        color='segment'
    )
    fig.update_layout(
        font=dict(
            family="Courier New, monospace",
            size=20,
            color="#00BFFF"
        ),
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=False
    )
    offline.plot(fig, filename='graphic_html.html', auto_open=False, include_plotlyjs='cdn')
    
 # Тестовые данные   
test_x = ['5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00']
test_y = [-6, -4, -2, 0, 1, 3, 5, 7]

construct_graphic(coor_x=test_x, coor_y=test_y) 
    