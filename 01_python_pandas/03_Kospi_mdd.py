# MDD(최대 손실 낙폭)
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

kospi = pdr.get_data_yahoo("^KS11", "2004-01-04")  # 코스피 데이터 지수 다운로드

window = 252  # 산정기간(1년 동안 개장일) 252일로 어림잡아 계산
# 코스피 종가 칼럼에서 1년 기간 단위로 최고치 peak 구한다
peak = kospi["Adj Close"].rolling(window, min_periods=1).max()
# drawdown은 최고치 대비 현재 코스피 종가가 얼마나 하락했는지 구한다
drawdown = kospi["Adj Close"] / peak - 1.0
# drawdown에서 1년 기간 단위로 최저치(max_dd)를 구한다 > 마이너스 값이라 최저치가 바로 최대 손실 낙폭이다
max_dd = drawdown.rolling(window, min_periods=1).min()

plt.figure(figsize=(9, 7))
plt.subplot(211)  # 2행 1열 중 1행에 그린다
kospi["Close"].plot(label="KOSPI", title="KOSPI MDD", grid=True, legend=True)
plt.subplot(212)  # 2행 1열 중 2행에 그린다
drawdown.plot(c="blue", label="KOSPI DD", grid=True, legend=True)
max_dd.plot(c="red", label="KOSPI MDD", grid=True, legend=True)
plt.show()
