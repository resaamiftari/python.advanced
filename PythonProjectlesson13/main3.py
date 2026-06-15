import pandas as pd

data={'name':["Resa","Donjeta","Aniku"],
       'age':[18,55,58],
      'City':["Viti","Malisheve","Deqan"]
       }

df=pd.DataFrame(data)
print(df)

fajlli=pd.read_csv("data.csv")
print(fajlli)

teDhenat=fajlli.to_csv("data.csv",index=False)
print(teDhenat)
