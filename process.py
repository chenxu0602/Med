import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dateparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d")
#df = pd.read_excel("回肠病变.xls", parse_dates=["检查日期"], date_parser=dateparse)
df = pd.read_excel("回肠病变.xls")
df_新增 = pd.read_excel("无复诊_新增确诊.xlsx")

null_内镜诊断 = df["内镜诊断"].isnull()
null_病理诊断 = df["病理诊断"].isnull()
df = df[~(null_内镜诊断 | null_病理诊断)]
df.drop_duplicates(subset=["姓名", "检查日期"], keep="first", inplace=True)
df["age"] = df["年龄"].str.replace("岁", "").astype(int)

"""
内镜诊断_问号 = df["内镜诊断"].str.contains(chr(65311))
内镜诊断_未明 = df["内镜诊断"].str.contains("未明")
内镜诊断_可能 = df["内镜诊断"].str.contains("可能")
内镜诊断_待排 = df["内镜诊断"].str.contains("待排")
内镜诊断_鉴别 = df["内镜诊断"].str.contains("鉴别")

未诊断 = 内镜诊断_问号 | 内镜诊断_未明 | 内镜诊断_可能 | 内镜诊断_待排 | 内镜诊断_鉴别 
df["未诊断"] = 未诊断.astype(int)

df_未诊断 = df[df["未诊断"]==True]
"""

"""
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
"""

name_count = df.groupby("姓名")["姓名"].count() 
dup_names = set(name_count[name_count > 1].index)
df_无复诊 = df[~df["姓名"].isin(dup_names)] 
df_复诊 = df[df["姓名"].isin(dup_names)] 

print(f"无复诊病例: {len(df_无复诊)}")
print(f"复诊病例: {len(set(df_复诊.index.get_level_values(0)))}")

无复诊_内镜诊断_问号 = df_无复诊["内镜诊断"].str.contains(chr(65311))
无复诊_内镜诊断_未明 = df_无复诊["内镜诊断"].str.contains("未明")
无复诊_内镜诊断_可能 = df_无复诊["内镜诊断"].str.contains("可能")
无复诊_内镜诊断_待排 = df_无复诊["内镜诊断"].str.contains("待排")
无复诊_内镜诊断_鉴别 = df_无复诊["内镜诊断"].str.contains("鉴别")
无复诊_内镜诊断_除外 = df_无复诊["内镜诊断"].str.contains("除外")
无复诊_内镜诊断_考虑 = df_无复诊["内镜诊断"].str.contains("考虑")
无复诊_内镜诊断_排除 = df_无复诊["内镜诊断"].str.contains("排除")

无复诊_未确诊 = 无复诊_内镜诊断_问号 | 无复诊_内镜诊断_未明 | 无复诊_内镜诊断_可能 | 无复诊_内镜诊断_待排 | 无复诊_内镜诊断_鉴别  \
                | 无复诊_内镜诊断_除外 | 无复诊_内镜诊断_考虑 | 无复诊_内镜诊断_排除

print(f"无复诊_内镜诊断_问号: {无复诊_内镜诊断_问号.sum()}")
print(f"无复诊_内镜诊断_未明: {无复诊_内镜诊断_未明.sum()}")
print(f"无复诊_内镜诊断_可能: {无复诊_内镜诊断_可能.sum()}")
print(f"无复诊_内镜诊断_待排: {无复诊_内镜诊断_待排.sum()}")
print(f"无复诊_内镜诊断_鉴别: {无复诊_内镜诊断_鉴别.sum()}")
print(f"无复诊_内镜诊断_除外: {无复诊_内镜诊断_除外.sum()}")
print(f"无复诊_内镜诊断_考虑: {无复诊_内镜诊断_考虑.sum()}")
print(f"无复诊_内镜诊断_排除: {无复诊_内镜诊断_排除.sum()}")
print(f"无复诊_未确诊: {无复诊_未确诊.sum()}")

df_无复诊["未确诊"] = 无复诊_未确诊.astype(int)
df_无复诊.loc[df_无复诊["未确诊"]==True].to_excel("无复诊_未确诊.xlsx", index=False)

df_无复诊_确诊 = df_无复诊.loc[df_无复诊["未确诊"]==False]
df_新增["未确诊"] = True

df_无复诊_确诊 = pd.concat([df_无复诊_确诊, df_新增])

parts = ["回末", "回肠", "小肠", "回肠末端"]
cancer = ["癌", "肿瘤", "肿物"]
inflation = ["炎", "糜烂"]

无复诊_确诊_内镜诊断_回肠炎_or_回末炎 = df_无复诊_确诊["内镜诊断"].str.contains('|'.join(parts)) & df_无复诊_确诊["内镜诊断"].str.contains('|'.join(inflation))
无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡 = df_无复诊_确诊["内镜诊断"].str.contains('|'.join(parts)) & df_无复诊_确诊["内镜诊断"].str.contains("溃疡")
无复诊_确诊_内镜诊断_结核 = df_无复诊_确诊["内镜诊断"].str.contains("结核")
无复诊_确诊_内镜诊断_淋巴瘤 = df_无复诊_确诊["内镜诊断"].str.contains("淋巴瘤")
无复诊_确诊_内镜诊断_滤泡 = df_无复诊_确诊["内镜诊断"].str.contains("滤泡")
无复诊_确诊_内镜诊断_嗜酸 = df_无复诊_确诊["内镜诊断"].str.contains("嗜酸")
无复诊_确诊_内镜诊断_克罗恩 = df_无复诊_确诊["内镜诊断"].str.contains("克罗") | df_无复诊_确诊["内镜诊断"].str.contains("克隆") | df_无复诊_确诊["内镜诊断"].str.contains("rohn")
无复诊_确诊_内镜诊断_息肉 = df_无复诊_确诊["内镜诊断"].str.contains("回末息肉") | df_无复诊_确诊["内镜诊断"].str.contains("回肠息肉") \
                      | df_无复诊_确诊["内镜诊断"].str.contains("小肠息肉") | df_无复诊_确诊["内镜诊断"].str.contains("回肠末端息肉")
无复诊_确诊_内镜诊断_寄生虫 = df_无复诊_确诊["内镜诊断"].str.contains("寄生虫")
无复诊_确诊_内镜诊断_癌 = df_无复诊_确诊["内镜诊断"].str.contains('|'.join(parts)) & df_无复诊_确诊["内镜诊断"].str.contains('|'.join(cancer))
无复诊_确诊_内镜诊断_白塞 = df_无复诊_确诊["内镜诊断"].str.contains("白塞")
无复诊_确诊_内镜诊断_淀粉 = df_无复诊_确诊["内镜诊断"].str.contains("淀粉")
无复诊_确诊_内镜诊断_小肠淋巴管扩张 = df_无复诊_确诊["内镜诊断"].str.contains("小肠淋巴管扩张")

print(f"无复诊_确诊_内镜诊断_回肠炎_or_回末炎: {无复诊_确诊_内镜诊断_回肠炎_or_回末炎.sum()}")
print(f"无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡: {无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡.sum()}")
print(f"无复诊_确诊_内镜诊断_结核: {无复诊_确诊_内镜诊断_结核.sum()}")
print(f"无复诊_确诊_内镜诊断_淋巴瘤: {无复诊_确诊_内镜诊断_淋巴瘤.sum()}")
print(f"无复诊_确诊_内镜诊断_滤泡: {无复诊_确诊_内镜诊断_滤泡.sum()}")
print(f"无复诊_确诊_内镜诊断_嗜酸: {无复诊_确诊_内镜诊断_嗜酸.sum()}")
print(f"无复诊_确诊_内镜诊断_克罗恩: {无复诊_确诊_内镜诊断_克罗恩.sum()}")
print(f"无复诊_确诊_内镜诊断_息肉: {无复诊_确诊_内镜诊断_息肉.sum()}")
print(f"无复诊_确诊_内镜诊断_寄生虫: {无复诊_确诊_内镜诊断_寄生虫.sum()}")
print(f"无复诊_确诊_内镜诊断_癌: {无复诊_确诊_内镜诊断_癌.sum()}")
print(f"无复诊_确诊_内镜诊断_白塞: {无复诊_确诊_内镜诊断_白塞.sum()}")
print(f"无复诊_确诊_内镜诊断_淀粉: {无复诊_确诊_内镜诊断_淀粉.sum()}")
print(f"无复诊_确诊_内镜诊断_小肠淋巴管扩张: {无复诊_确诊_内镜诊断_小肠淋巴管扩张.sum()}")

没病 = ~(
        无复诊_确诊_内镜诊断_回肠炎_or_回末炎 \
      | 无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡 \
      | 无复诊_确诊_内镜诊断_结核 \
      | 无复诊_确诊_内镜诊断_淋巴瘤 \
      | 无复诊_确诊_内镜诊断_滤泡 \
      | 无复诊_确诊_内镜诊断_嗜酸 \
      | 无复诊_确诊_内镜诊断_克罗恩 \
      | 无复诊_确诊_内镜诊断_息肉 \
      | 无复诊_确诊_内镜诊断_寄生虫 \
      | 无复诊_确诊_内镜诊断_癌 \
      | 无复诊_确诊_内镜诊断_白塞 \
      | 无复诊_确诊_内镜诊断_淀粉 \
      | 无复诊_确诊_内镜诊断_小肠淋巴管扩张 \
      )

df_无复诊_确诊_没病 = df_无复诊_确诊[没病]
df_无复诊_确诊_没病.to_excel("无复诊_确诊_没病.xlsx", index=False)

df_无复诊_确诊["无复诊_确诊_内镜诊断_回肠炎_or_回末炎"] = 无复诊_确诊_内镜诊断_回肠炎_or_回末炎.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡"] = 无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_结核"] = 无复诊_确诊_内镜诊断_结核.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_淋巴瘤"] = 无复诊_确诊_内镜诊断_淋巴瘤.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_滤泡"] = 无复诊_确诊_内镜诊断_滤泡.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_嗜酸"] = 无复诊_确诊_内镜诊断_嗜酸.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_克罗恩"] = 无复诊_确诊_内镜诊断_克罗恩.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_息肉"] = 无复诊_确诊_内镜诊断_息肉.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_寄生虫"] = 无复诊_确诊_内镜诊断_寄生虫.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_癌"] = 无复诊_确诊_内镜诊断_癌.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_白塞"] = 无复诊_确诊_内镜诊断_白塞.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_淀粉"] = 无复诊_确诊_内镜诊断_淀粉.astype(int)
df_无复诊_确诊["无复诊_确诊_内镜诊断_小肠淋巴管扩张"] = 无复诊_确诊_内镜诊断_小肠淋巴管扩张.astype(int)

df_无复诊_确诊["Total"] = df_无复诊_确诊["无复诊_确诊_内镜诊断_回肠炎_or_回末炎"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_结核"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_淋巴瘤"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_滤泡"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_嗜酸"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_克罗恩"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_息肉"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_寄生虫"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_癌"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_白塞"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_淀粉"] \
                      + df_无复诊_确诊["无复诊_确诊_内镜诊断_小肠淋巴管扩张"] \


df_无复诊_确诊.loc[df_无复诊_确诊["Total"] > 1, ["姓名", "检查日期", "Total", "内镜诊断", "病理诊断"]].to_excel("无复诊_确诊_多病.xlsx", index=False)

复诊_确诊_内镜诊断_回肠炎_or_回末炎 = df_复诊["内镜诊断"].str.contains('|'.join(parts)) & df_复诊["内镜诊断"].str.contains('|'.join(inflation))
复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡 = df_复诊["内镜诊断"].str.contains('|'.join(parts)) & df_复诊["内镜诊断"].str.contains("溃疡")
复诊_确诊_内镜诊断_结核 = df_复诊["内镜诊断"].str.contains("结核")
复诊_确诊_内镜诊断_淋巴瘤 = df_复诊["内镜诊断"].str.contains("淋巴瘤")
复诊_确诊_内镜诊断_滤泡 = df_复诊["内镜诊断"].str.contains("滤泡")
复诊_确诊_内镜诊断_嗜酸 = df_复诊["内镜诊断"].str.contains("嗜酸")
复诊_确诊_内镜诊断_克罗恩 = df_复诊["内镜诊断"].str.contains("克罗") | df_复诊["内镜诊断"].str.contains("克隆") | df_复诊["内镜诊断"].str.contains("rohn")
复诊_确诊_内镜诊断_息肉 = df_复诊["内镜诊断"].str.contains("回末息肉") | df_复诊["内镜诊断"].str.contains("回肠息肉") \
                      | df_复诊["内镜诊断"].str.contains("小肠息肉") | df_复诊["内镜诊断"].str.contains("回肠末端息肉")
复诊_确诊_内镜诊断_寄生虫 = df_复诊["内镜诊断"].str.contains("寄生虫")
复诊_确诊_内镜诊断_癌 = df_复诊["内镜诊断"].str.contains('|'.join(parts)) & df_复诊["内镜诊断"].str.contains('|'.join(cancer))
复诊_确诊_内镜诊断_白塞 = df_复诊["内镜诊断"].str.contains("白塞")
复诊_确诊_内镜诊断_淀粉 = df_复诊["内镜诊断"].str.contains("淀粉")
复诊_确诊_内镜诊断_小肠淋巴管扩张 = df_复诊["内镜诊断"].str.contains("小肠淋巴管扩张")

df_复诊["复诊_确诊_内镜诊断_回肠炎_or_回末炎"] = 复诊_确诊_内镜诊断_回肠炎_or_回末炎.astype(int)
df_复诊["复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡"] = 复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡.astype(int)
df_复诊["复诊_确诊_内镜诊断_结核"] = 复诊_确诊_内镜诊断_结核.astype(int)
df_复诊["复诊_确诊_内镜诊断_淋巴瘤"] = 复诊_确诊_内镜诊断_淋巴瘤.astype(int)
df_复诊["复诊_确诊_内镜诊断_滤泡"] = 复诊_确诊_内镜诊断_滤泡.astype(int)
df_复诊["复诊_确诊_内镜诊断_嗜酸"] = 复诊_确诊_内镜诊断_嗜酸.astype(int)
df_复诊["复诊_确诊_内镜诊断_克罗恩"] = 复诊_确诊_内镜诊断_克罗恩.astype(int)
df_复诊["复诊_确诊_内镜诊断_息肉"] = 复诊_确诊_内镜诊断_息肉.astype(int)
df_复诊["复诊_确诊_内镜诊断_寄生虫"] = 复诊_确诊_内镜诊断_寄生虫.astype(int)
df_复诊["复诊_确诊_内镜诊断_癌"] = 复诊_确诊_内镜诊断_癌.astype(int)
df_复诊["复诊_确诊_内镜诊断_白塞"] = 复诊_确诊_内镜诊断_白塞.astype(int)
df_复诊["复诊_确诊_内镜诊断_淀粉"] = 复诊_确诊_内镜诊断_淀粉.astype(int)
df_复诊["复诊_确诊_内镜诊断_小肠淋巴管扩张"] = 复诊_确诊_内镜诊断_小肠淋巴管扩张.astype(int)

df_复诊.set_index(["姓名", "检查日期"], inplace=True)
df_复诊.sort_index(inplace=True)

results = set()

复诊时间 = {}

复诊年龄 = []

for name in dup_names:
    df_复诊_病人 = df_复诊.xs(name, level=0)
    复诊年龄.append(df_复诊_病人.iloc[0].age)
    data = df_复诊_病人[[
        "复诊_确诊_内镜诊断_回肠炎_or_回末炎", 
        "复诊_确诊_内镜诊断_回肠溃疡_or_回末溃疡",
        "复诊_确诊_内镜诊断_结核",
        "复诊_确诊_内镜诊断_淋巴瘤",
        "复诊_确诊_内镜诊断_滤泡",
        "复诊_确诊_内镜诊断_嗜酸",
        "复诊_确诊_内镜诊断_克罗恩",
        "复诊_确诊_内镜诊断_息肉",
        "复诊_确诊_内镜诊断_寄生虫",
        "复诊_确诊_内镜诊断_癌",
        "复诊_确诊_内镜诊断_白塞",
        "复诊_确诊_内镜诊断_淀粉",
        "复诊_确诊_内镜诊断_小肠淋巴管扩张"]].values
    for i in range(1, len(data)):
        if not all(np.equal(data[i-1], data[i])):
            break
    else:
#        print(name)
        results.add(name)

    dates = pd.to_datetime(df_复诊_病人.index)
    n_intervals, tot_intervals = 0, 0
    for i in range(1, len(dates)):
        interval = (dates[i] - dates[i-1]).days
        if interval >= 30:
            n_intervals += 1
            tot_intervals += interval
    if n_intervals > 0:
        avg_interval = tot_intervals // n_intervals
        print(f"{name}: 平均{avg_interval}天, {n_intervals}个间隔")
        复诊时间[name] = avg_interval
    else:
        print(f"{name}: 无复诊")

intervals = np.array(list(复诊时间.values()))
print(f"平均复诊时间: {np.mean(intervals)}+-{np.std(intervals)}")

df_癌症 = pd.concat([df_无复诊_确诊.loc[df_无复诊_确诊["无复诊_确诊_内镜诊断_癌"]==1].reset_index(),
                    df_复诊.loc[df_复诊["复诊_确诊_内镜诊断_癌"]==1].reset_index()])
df_癌症.to_excel("癌症.xlsx", index=False)
                    