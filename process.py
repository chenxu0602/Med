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

病理诊断_炎_or_溃疡 = df["病理诊断"].str.contains("炎") | df["病理诊断"].str.contains("溃疡")
病理诊断_结核 = df["病理诊断"].str.contains("结核")
病理诊断_抗酸染色阴性 = df["病理诊断"].str.contains("抗酸染色阴性")
病理诊断_克罗恩_or_Crohn_or_克隆氏 = df["病理诊断"].str.contains("克罗恩") | df["病理诊断"].str.contains("Crohn") | df["病理诊断"].str.contains("克隆氏")
病理诊断_淋巴滤泡 = df["病理诊断"].str.contains("淋巴滤泡")
病理诊断_寄生虫 = df["病理诊断"].str.contains("寄生虫")
病理诊断_淀粉样变性 = df["病理诊断"].str.contains("淀粉样变性")
病理诊断_淋巴管扩展 = df["病理诊断"].str.contains("淋巴管扩展")

df["病理诊断_炎_or_溃疡"] = 病理诊断_炎_or_溃疡.astype(int)
df["病理诊断_结核"] = 病理诊断_结核.astype(int)
df["病理诊断_抗酸染色阴性"] = 病理诊断_抗酸染色阴性.astype(int)
df["病理诊断_克罗恩_or_Crohn_or_克隆氏"] = 病理诊断_克罗恩_or_Crohn_or_克隆氏.astype(int)
df["病理诊断_淋巴滤泡"] = 病理诊断_淋巴滤泡.astype(int)
df["病理诊断_寄生虫"] = 病理诊断_寄生虫.astype(int)
df["病理诊断_淀粉样变性"] = 病理诊断_淀粉样变性.astype(int)
df["病理诊断_淋巴管扩展"] = 病理诊断_淋巴管扩展.astype(int)

df.sort_values(by=["姓名", "检查日期"], inplace=True)
df.to_excel("内镜诊断.xlsx", index=False)

name_count = df.groupby("姓名")["姓名"].count() 
dup_names = set(name_count[name_count > 1].index)
df_dup = df[df["姓名"].isin(dup_names)] 
df_dup.to_excel("复诊病人.xlsx", index=False)