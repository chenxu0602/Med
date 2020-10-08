import pandas as pd

df = pd.read_excel("数据.xlsx")
df.set_index("姓名", inplace=True)

df_BMI_std = (df["BMI"] - df["BMI"].mean()) / df["BMI"].std()