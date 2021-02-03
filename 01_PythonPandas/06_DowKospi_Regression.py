# 다우존스 지수와 코스피의 선형 회귀 분석
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스, 코스피 지수 데이터 야후 파이낸스에서 다운로드
dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")

# 다우존스 지수를 X 칼럼으로 코스피 지수를 Y 칼럼으로 갖는 데이터프레임 생성
df = pd.DataFrame({"X": dow["Close"], "Y": kospi["Close"]})
df = df.fillna(method="bfill")  # 모든 NaN 제거
df = df.fillna(method="ffill")

regr = stats.linregress(df.X, df.Y)  # X와 Y로 선형회귀 모델 객체 regr 생성
# 범례에 회귀식 표시하는 레이블 문자
regr_line = f"Y ={regr.slope:.2f} * X + {regr.intercept:.2f}"

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, ".")  # 산점도를 작은 원으로 나타낸다
plt.plot(df.X, regr.slope * df.X + regr.intercept, "r")  # 회귀선을 붉은 색으로 그린다
plt.legend(["DOW X KOSPI", regr_line])
plt.title(f"DOW X KOSPI (R= {regr.rvalue:.2f})")
plt.xlabel("Dow Jones Industrial Average")
plt.ylabel("KOSPI")
plt.show()
