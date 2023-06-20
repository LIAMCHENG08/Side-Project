import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data=pd.read_csv('yoy.csv',encoding=('ANSI'))
x=data.iloc[:,0]
y=data.iloc[:,1:3]
y.columns=['exchange_rate','yoy']

#中文基本設定
plt.rcParams['font.family']='Microsoft YaHei'
# 等比例放大

plt.figure(dpi=1200)
#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(16, 10), facecolor='white')
# plt.figure(figsize=(12,8),facecolor=('lightblue'))

plt.minorticks_on()
#傾斜
plt.xticks(np.arange(0, len(x),4),x[::4], rotation=45)
plt.plot(x,y['yoy'],'g-.')
plt.title('經濟成長率(%)',size=25)
plt.xlabel('年度',fontsize=20)
plt.ylabel('經濟成長率(%)',fontsize=20)
plt.grid()

plt.xlim(left=0,right=x[24])
# plt.gca().invert_xaxis()
plt.savefig('yoy(%).png')
plt.show()