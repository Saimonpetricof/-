import pandas as pd
import numpy as np

def num_distinct(df: pd.DataFrame) -> int:
    """
    Подсчитайте количество отсутствующих значений в столбце `product`.

    Например, для такого датафрейма

    id    product
    100   apple
    101   orange
    102   <NA>
    
    нужно вернуть 1.
    """
    

#   print(num_distinct(pd.DataFrame({"id": [1,2,100], "product":[np.nan,1,np.nan]})))

    return df["product"].isna().sum()


