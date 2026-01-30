import pandas as pd

data = {"A" : [1,2,2,1],
        "B" : [3.1,4.2,1.5,6.3],
        "C" : [800,150,400,210]}

df = pd.DataFrame(data)    #creating the DataFrame

df["Total"] = df["A"] * df["B"] + df["C"]     #adding a new derived column

print(df)