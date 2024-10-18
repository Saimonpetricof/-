import pandas as pd
import numpy as np
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
    dfn = df['product'].fillna(pd.NA).dropna()
    return len(np.unique(dfn.to_numpy()))
