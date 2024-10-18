import pandas as pd

def count_rows(df: pd.DataFrame) -> int:
    """
    Подсчитайте количество строк в датафрейме.

    Например, для такого датафрейма

    id    product
    100   apple
    101   orange
    102   pineapple
    
    нужно вернуть 3.
    """

    return 