import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('pop.csv',encoding=('ANSI'))

y=data.loc[1,'2013':]


#中文基本設定
plt.rcParams['font.family']='Microsoft YaHei'
# 等比例放大
plt.figure(dpi=1200)
#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(16, 10), facecolor='white')
# plt.figure(figsize=(12,8),facecolor=('lightblue'))

plt.minorticks_on()
#傾斜
plt.xticks(np.arange(0, len(y),2),y.index[0::2], rotation=45)
plt.plot(y.index,y,'g-.')
plt.title('15-64歲人口數',size=25)
plt.xlabel('年度',fontsize=20)
plt.ylabel('人口數\n(千人)',fontsize=20,ha='right',rotation=0)
plt.grid()
plt.xlim(left=0,right=y.index[-1])

plt.savefig('pop.png')
plt.show()

