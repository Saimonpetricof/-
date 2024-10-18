import pandas as pd
import numpy as np
def test1(Solution) -> bool:
		
		Ans = [1 ,1, 2, 2]
		Problem = [pd.DataFrame({"id": [1,2,100], "product":[1,1,1]}), 
						   pd.DataFrame({"id": [1,2,100], "product":[pd.NA,pd.NA,pd.NA]}),
							 pd.DataFrame({"id": [1,2,100], "product":[pd.NA,1,pd.NA]}),
							 pd.DataFrame({"id": [1,2,100], "product":[np.nan,1,np.nan]})]
		
		for index, ans in enumerate(Ans):
				assert (Solution(Problem[index])) == ans