from typing import Any
import pandas as pd

def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    В датафрейме с продажами некоторые цены пропущены.

    id  product   price
    432 apple     32.1
    433 orange    67.3
    444 apple     -
    445 pineapple 102
    446 apple     34.1  

    Надо заполнить пропуски средними значениями, соответствующими типу товара. То есть пропуски цен у яблок 
    должны заполняться средней ценой яблок, и т.д.

    Так пропуск в приведённом выше датафрейме нужно заполнить числом 33.1.

    Исходный DataFrame должен остаться неизменным.
    """

    return