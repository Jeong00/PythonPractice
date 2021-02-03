# 지수화로 다우존스 지수와 코스피 비교하기
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스 지수 데이터 야후 파이낸스에서 다운로드
dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
# 2000년 이후 코스피 지수 데이터 야후 파이낸스에서 다운로드
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")

# 지수화(금일 다우존스 지수를 000104일 다우존스 지수로 나눈 뒤 100곱함)
d = (dow.Close / dow.Close.loc["2000-01-04"]) * 100
# 지수화(금일 코스피 지수를 000104일 코스피 지수로 나눈 뒤 100곱함)
k = (kospi.Close / kospi.Close.loc["2000-01-04"]) * 100

plt.figure(figsize=(9, 5))
plt.plot(d.index, d, "r--",
         label="Dow Jones Industrial")  # 다우존스 붉은 점선으로 출력
plt.plot(k.index, k, "b", label="KOSPI")  # 코스피 푸른 실선으로 출력
plt.grid(True)
plt.legend(loc="best")
plt.show()
