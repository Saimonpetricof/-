import pandas as pd
import numpy as np

def test1(Solution) -> bool:
		
		Ans = [0 ,2, 0, 2]
		Problem = [pd.DataFrame({"id": [1,2,100], "product":["      ","  1   "," 89   "]}), 
						   pd.DataFrame({"id": [1,2,100], "product":["pd.NAN","123456","ffeer"]}),
							 pd.DataFrame({"id": [1,2,100], "product":["34532","1","sf"]}),
							 pd.DataFrame({"id": [1,2,100], "product":["np.nan","132 345","np.nan"]})]
		
		for index, ans in enumerate(Ans):
				assert (Solution(Problem[index])) == ans