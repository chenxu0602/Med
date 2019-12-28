import pandas as pd
import matplotlib.pyplot as plt

dateparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d")
df = pd.read_excel("回肠病变.xls", parse_dates=["检查日期"], date_parser=dateparse)
df["age"] = df["年龄"].str.replace("岁", "").astype(int)

null_内镜诊断 = df["内镜诊断"].isnull()
null_病理诊断 = df["病理诊断"].isnull()

df = df[~(null_内镜诊断 | null_病理诊断)]

内镜诊断_回肠炎_or_回末炎 = df["内镜诊断"].str.contains("回肠炎") | df["内镜诊断"].str.contains("回末炎")
内镜诊断_回肠溃疡_or_回末溃疡 = df["内镜诊断"].str.contains("回肠溃疡") | df["内镜诊断"].str.contains("回末溃疡")
内镜诊断_结核 = df["内镜诊断"].str.contains("结核")
内镜诊断_淋巴瘤 = df["内镜诊断"].str.contains("淋巴瘤")
内镜诊断_淋巴滤泡 = df["内镜诊断"].str.contains("淋巴滤泡")
内镜诊断_嗜酸 = df["内镜诊断"].str.contains("嗜酸")
内镜诊断_克罗恩 = df["内镜诊断"].str.contains("克罗恩")
内镜诊断_息肉 = df["内镜诊断"].str.contains("息肉")

df["内镜诊断_回肠炎_or_回末炎"] = 内镜诊断_回肠炎_or_回末炎.astype(int)
df["内镜诊断_回肠溃疡_or_回末溃疡"] = 内镜诊断_回肠溃疡_or_回末溃疡.astype(int)
df["内镜诊断_结核"] = 内镜诊断_结核.astype(int)
df["内镜诊断_淋巴瘤"] = 内镜诊断_淋巴瘤.astype(int)
df["内镜诊断_淋巴滤泡"] = 内镜诊断_淋巴滤泡.astype(int)
df["内镜诊断_嗜酸"] = 内镜诊断_嗜酸.astype(int)
df["内镜诊断_克罗恩"] = 内镜诊断_克罗恩.astype(int)
df["内镜诊断_息肉"] = 内镜诊断_息肉.astype(int)

df.sort_values(by=["姓名", "检查日期"]).to_excel("内镜诊断.xlsx", index=False)