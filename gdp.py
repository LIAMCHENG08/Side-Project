import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('newgdp.csv',encoding=('ANSI'))
y=data.loc[4:,'國內生產毛額GDP(名目值，百萬美元)']
year=data.iloc[4:,0]
#中文基本設定
plt.rcParams['font.family']='Microsoft YaHei'
# 等比例放大
plt.figure(dpi=1200)
#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(16,10), facecolor='white')

plt.minorticks_on()
#傾斜
# 設定x軸範圍，讓第一筆資料在y軸上
plt.xlim(left=0)
# 
plt.xticks(np.arange(0, len(year)), rotation=45)
plt.plot(year,y,'g-.')

plt.title('國內生產毛額GDP(名目值，百萬美元)',size=25)
plt.xlabel('年度',size=20)
plt.ylabel('GDP(百萬美元)',fontsize=20,ha='left')

plt.savefig('GDP.png')
plt.show()