import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('debitcarry.csv',encoding=('ANSI'))
data.columns=['yearQ','debit_rate']


#中文基本設定
plt.rcParams['font.family']='Microsoft YaHei'
# 等比例放大

plt.figure(dpi=1200)
#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(16, 10), facecolor='white')
# plt.figure(figsize=(12,8),facecolor=('lightblue'))

plt.minorticks_on()
#傾斜
plt.xticks(np.arange(0, len(data),4),data['yearQ'][::4], rotation=45)
plt.plot(data['yearQ'],data['debit_rate'],color='tab:blue')
plt.title('貸款負擔率',size=25)
plt.xlabel('年度季度',fontsize=20)
plt.ylabel('貸款負擔率(%)',fontsize=20)
plt.grid()

plt.xlim(left=0,right=data['yearQ'][83])
plt.gca().invert_xaxis()
plt.savefig('debitcarry.png')
plt.show()
