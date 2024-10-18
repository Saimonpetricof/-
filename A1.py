import pandas as pd

def num_distinct(df: pd.DataFrame) -> int:
    """
    Подсчитайте количество уникальных значений в столбце `product`.

    Например, для такого датафрейма

    id    product
    100   apple
    101   orange
    102   apple
    
    нужно вернуть 2.
    """

    return