from typing import Any
import pandas as pd

def count_low_high(df: pd.DataFrame) -> pd.DataFrame:
    """
    Дан датафрейм вида

    df = pd.DataFrame({
        'col1': ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a'],
        'col2': [1, 2, 1, 4, 5, 6, 6, 6, 9, 1],
        'col3': ['LOW', 'HIGH', 'LOW', 'LOW', 'HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH', 'HIGH'],
    })

    Для каждой группы строк с одинаковым значением col1 необходимо посчитать количество 
    уникальных значений в столбце col2 для тех строк группы, где col3 равен LOW, и сохранить 
    это значение в новом столбце 'low_count'. Аналогично для HIGH и high_count.

    Так для датафрейма, приведённого выше, результат будет 

    pd.DataFrame({
        'col1': ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a'],
        'col2': [1, 2, 1, 4, 5, 6, 6, 6, 9, 1],
        'col3': ['LOW', 'HIGH', 'LOW', 'LOW', 'HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH', 'HIGH'],
        'low-count': [1, 1, 2, 2, 2, 1, 1, 1, 1, 1],
        'high-count': [2, 2, 1, 1, 1, 2, 2, 2, 2, 2],
    })

    Возвращает новый датафрейм (не трогает исходный).
    """

    return