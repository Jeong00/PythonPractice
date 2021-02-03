# 산점도로 다우존스 지수와 코스피의 관계분석
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스 지수 데이터 야후 파이낸스에서 다운로드
dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
# 2000년 이후 코스피 지수 데이터 야후 파이낸스에서 다운로드
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")

# 다우존스와 코스피의 길이
print(len(dow))
print(len(kospi))

# 다우존스 지수의 종가칼럼과 코스피지수의 종가칼럼을 합쳐서 데이터프레임 생성
df = pd.DataFrame({"DOW": dow["Close"], "KOSPI": kospi["Close"]})
df = df.fillna(method="bfill")  # 모든 NaN 제거
df = df.fillna(method="ffill")

plt.figure(figsize=(7, 7))
# 산점도를 그리려면 데이터의 개수가 동일해야만 한다 & NaN 없어야함
# 다우존스 지수를 x로 코스피를 y로 산점도를 그리되 점은 작은 원모양(.)으로 표시한다
plt.scatter(df["DOW"], df["KOSPI"], marker=".")
plt.xlabel("Dow Jones Industrial Average")
plt.ylabel("KOSPI")
plt.show()
