import pandas as pd
import numpy as np
from A2 import num_distinct

def test1(num_distinct):	
		Ans = [0 ,3, 2, 6, 100, 0]
		Problem = [pd.DataFrame({"id": [1,2,100], "product":[1,2,3]}), 
						   	pd.DataFrame({"id": [1,2,100], "product":[pd.NA,pd.NA,pd.NA]}),
							pd.DataFrame({"cost": [1,2,100], "product":[pd.NA,1,pd.NA]}),
							pd.DataFrame({"kot": [i for i in range(9)], "product":[np.nan,1,np.nan]*3}),
							pd.DataFrame({"product":[pd.NA]*100}),
							pd.DataFrame({"lor": [], "product":[]})
							]
		
		for index, ans in enumerate(Ans):
				assert (num_distinct(Problem[index])) == ans
