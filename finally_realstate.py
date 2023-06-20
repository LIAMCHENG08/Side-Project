import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('real_state_index.csv', encoding='ANSI')
x = data.iloc[:, 0]

y = data.iloc[:, 1:]

plt.rcParams['font.family'] = 'Microsoft YaHei'

# 等比例放大
plt.figure(dpi=1200)
#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(16, 10), facecolor='white')
#刻度
plt.minorticks_on()
#傾斜
plt.xticks(np.arange(0, len(x), 4),x[::4], rotation=45)


plt.plot(x,y.iloc[:,:],label=data.columns[1:])

plt.title('住宅價格季指數',size=25)
plt.xlabel('年度季度',fontsize=20)
plt.ylabel('''指數''',fontsize=20,ha='right',rotation=0)
plt.legend()
plt.xlim(left=0,right=x.iloc[-1])

#x 軸反轉
plt.gca().invert_xaxis()

plt.grid(axis="y")
plt.grid(axis='x')
plt.savefig('realestateindex.png')
plt.show()

