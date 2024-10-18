import pandas as pd

def num_distinct(df: pd.DataFrame) -> int:
    """
    Подсчитайте количество значений в столбце `product` с длиной строки 
    строго больше 5.

    Например, для такого датафрейма

    id    product
    100   apple
    101   orange
    102   pineapple
    
    нужно вернуть 2.
    """

    return