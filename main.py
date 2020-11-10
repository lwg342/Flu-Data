# -> Created on 10 November 2020
# -> Author: Weiguang Liu

# %%
import pandas as pd
from wl_regression import BSpline
import numpy as np
# %% 
DF =pd.read_excel('Summary.xlsx')
TS = pd.pivot_table(data=DF, values ='mCherry', index='Time (h)', columns = 'Sample')
# %%
List = DF.Sample.unique()
List# %%
# %%
for i in List:
    X = TS.index
    M = BSpline(X, TS[i], 2).fit()
    import matplotlib.pyplot as plt
    plt.plot(X, TS[i])
    plt.plot(X, M)
# %%
# %%
np.len(X)
M1 = BSpline(X, TS[0],2).univariate_bspline_basis()

# %%
