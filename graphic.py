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
    df = pd.DataFrame({'x': coor_x, 'y': coor_y}) # Подходящий формат данных
    fig = px.line(
        df,
        x='x',
        y='y',  
        title='График погоды',
        markers=True,
        labels={'x': 'Время', 'y': 'Температура'}
    )
    offline.plot(fig, filename='graphic_html.html', auto_open=False, include_plotlyjs='cdn')
    
 # Тестовые данные   
test_x = ['5:00', '6:00', '7:00', '8:00', '9:00', '10:00,', '11:00', '12:00']
test_y = [-6, -4, -2, 0, 1, 3, 5, 7]

construct_graphic(coor_x=test_x, coor_y=test_y) 
    