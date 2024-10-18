from __future__ import annotations      # чтобы писать 'list' вместо 'typing.List' для python <3.9

import pandas as pd

def cap(df: pd.DataFrame) -> pd.DataFrame:
    """
    Дан датафрейм вида

      Name A B C D
    0 Jack 3 2 5 5
    1 Jack 4 9 7 7 
    2 Jack 6 0 1 3 
    3 Jill 7 0 7 9 
    4 Jill 1 3 9 1
    5 Jill 2 7 1 5

    Необходимо для каждой группы строк с одинаковым значением столбца Name
    определить максимальное значение в каждом из столбцов A, B и D и уменьшить
    такие значения на единицу. Столбец C менять не нужно.

    То есть для приведённого выше датафрейма должно получиться следующее:

      Name A B C D
    0 Jack 3 2 5 5
    1 Jack 4 8 7 6 
    2 Jack 5 0 1 3 
    3 Jill 6 0 7 8 
    4 Jill 1 3 9 1
    5 Jill 2 6 1 5     

    Возвращает новый датафрейм (не трогает исходный).
    """
    
    return
