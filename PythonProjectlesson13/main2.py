import pandas as pd

produktet=["molla","banane","portokaje","dardha","rrush"]

shitjet=[120,25,36,52,25]

sales_series=pd.Series(shitjet,index=produktet)
print(sales_series)

print(sales_series("molla"))

print(sales_series.sum())

print(sales_series.idmax())

