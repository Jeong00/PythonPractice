# 야후 파이낸스로 주식 시세 구하기
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()  # 이 함수와

# 이 함수를 사용해서 빠르게 데이터를 다운로드 할 수 있다
# 조회 시작일은 삼성전자 액면 분할 이후로 설정 / 조회 종료일은 생략해서 오늘 날짜로 지정됨
sec = pdr.get_data_yahoo("005930.KS", start="2018-05-04")
sec.dpc = (sec["Close"]-sec["Close"].shift(1)) / sec["Close"].shift(1) * 100
sec.dpc.iloc[0] = 0  # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다
sec.dpc_cs = sec.dpc.cumsum()  # 일간 변동률의 누적합을 구한다

tsla = pdr.get_data_yahoo("TSLA", start="2018-05-04")
tsla.dpc = (tsla["Close"] / tsla["Close"].shift(1) - 1) * 100
tsla.dpc.iloc[0] = 0
tsla.dpc_cs = tsla.dpc.cumsum()

plt.plot(sec.index, sec.dpc_cs, "b", label="Samsung Electronics")
plt.plot(tsla.index, tsla.dpc_cs, "r--", label="Tesla")
plt.ylabel("Change %")
plt.grid(True)
# 범례의 위치를 best로 지정하면, 그래프가 표시되지 않는 부분을 찾아서 적절한 위치에 범례를 표시해줌
plt.legend(loc="best")
plt.show()
