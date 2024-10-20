from typing import Any
import pandas as pd

def set_index_value(df: pd.DataFrame, i: int, val: Any) -> pd.DataFrame:
    """
    Изменяет i-е значение индекса датафрейма на заданное значение. Например,
    для такого датафрейма

                     FGE       FFI       FRA    FARCAD    FCOCAD                                                        
    date
    2020-12-31       NaN       NaN       NaN       NaN       NaN
    2021-12-31  0.137961 -0.040112  0.098811  0.062196  0.088000
    2022-12-31 -0.142319 -0.090379  0.068276  0.102470  0.095588
    2022-12-31  0.038630 -0.035256  0.067030  0.044813  0.037752

    set_index_value(df, -1, '2023-12-31') изменит '2022-12-31' на '2023-12-31'.

    Возвращает новый датафрейм (не трогает исходный).
    """

    return