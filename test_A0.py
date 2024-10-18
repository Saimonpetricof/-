import pandas as pd

from sample import count_rows

def test_count_rows():
    df = pd.DataFrame({'a': [1,2,3]})
    assert count_rows(df) == 3