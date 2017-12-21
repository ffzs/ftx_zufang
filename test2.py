import pandas as pd
import math

df = pd.read_csv("zufang.csv")
# print(df)
df["sqrt"] = 0
df["location"] =""
name_list = []
for i in range(0,len(df)):
    number = df.iat[i,4]
    name = df.iat[i,3].split("-")[0].strip()
    df.iat[i,6] = name
    df.iat[i, 5] = math.sqrt(int(number))
    if not name in name_list:
        name_list.append(name)
# print(number)
df.to_csv("zufang1.csv",encoding="utf-8")
print(name_list)


# print(df2)
