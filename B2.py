from typing import Any
import pandas as pd

def span(df: pd.DataFrame) -> pd.DataFrame:
    """
    Для каждого товара вычислите разницу максимальной и минимальной цены.

    Например, для такого датафрейма

    id  product   price
    432 apple     32.1
    433 orange    67.3
    444 apple     33.1
    445 orange    67.9
    446 apple     34.1  

    должно получиться
    
       product  span
    0  apple    2.0
    1  orange   0.6
    """

    return     