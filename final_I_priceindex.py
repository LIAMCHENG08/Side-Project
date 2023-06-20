import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

con = sqlite3.connect('f_crisis.db')
#建立 cursor 物件並顯示
cursor = con.execute('SELECT * FROM interest_rate')
#利率
#從cursor 物件取出所有資料
rows = cursor.fetchall()


data_interest_time = []
data_interest_rate = []
for row in rows:
    data_interest_time.append(row[0])
    data_interest_rate.append(row[1])


a = []
for i in data_interest_time:
    a.append([j for j in i.split('/')])
quarter1 = {'01': 'Q1', '02': 'Q1', '03': 'Q1'}
quarter2 = {'04': 'Q2', '05': 'Q2', '06': 'Q2'}
quarter3 = {'07': 'Q3', '08': 'Q3', '09': 'Q3'}
quarter4 = {'10': 'Q4', '11': 'Q4', '12': 'Q4'}
Q = []
for k in a:
    if k[1] in quarter1:
        k = k[0] + 'Q1'
        Q.append(k)
    elif k[1] in quarter2:
        k = k[0] + 'Q2'
        Q.append(k)
    elif k[1] in quarter3:
        k = k[0] + 'Q3'
        Q.append(k)
    elif k[1] in quarter4:
        k = k[0] + 'Q4'
        Q.append(k)

#兩個LIST TO DATAFRAME並轉置    
data = pd.DataFrame([Q, data_interest_rate]).T
#變更欄名
data.columns = ['yearQ', 'interest_rate']
#因為有重複的年份，所以把他GROUPBY取平均
yearq_n_interest_rate = data.groupby('yearQ')['interest_rate'].mean()

#建立 cursor 物件
cursor1 = con.execute('SELECT * FROM real_estate_index')
#房價指數
#從cursor1 物件取出所有資料
rows1 = cursor1.fetchall()
data_price_index = []
data_price_index_time = []
for row in rows1:
    data_price_index_time.append(row[0])
    data_price_index.append(row[1])
#兩個LIST TO DATAFRAME並轉置    
yearq_n_price_index = pd.DataFrame([data_price_index_time, data_price_index]).T
#變更欄名
yearq_n_price_index.columns = ['yearQ', 'price_index']

#因兩個資料的年份排序不一,所以我把他們排序變成一樣
final_yearq_n_price_index = yearq_n_price_index.sort_values('yearQ', ascending=True)

# 合併兩個資料變成一張DATAFRAME
final_alldata = pd.merge(final_yearq_n_price_index, yearq_n_interest_rate, on='yearQ')
#畫圖
#中文設定
plt.rcParams['font.family']='Microsoft YaHei'


# 繪製圖表
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

#圖一
ax1.plot(final_alldata['yearQ'], final_alldata['interest_rate'], color='#FF5733', label='利率(%)')
ax1.set_xlabel('年份')
ax1.set_ylabel('利率(%)', color='#FF5733')
#tick_params是一個用於設置刻度線和刻度標籤屬性的方法，通過指定axis='y'，表示設置y軸的刻度線和刻度標籤屬性
#為了讓利率標籤有顏色
ax1.tick_params(axis='y', labelcolor='#FF5733')

#圖二
ax2.plot(final_alldata['yearQ'], final_alldata['price_index'], color='tab:blue', label='全國住宅房價指數')
ax2.set_ylabel('全國住宅房價指數', color='tab:blue')
#tick_params是一個用於設置刻度線和刻度標籤屬性的方法，通過指定axis='y'，表示設置y軸的刻度線和刻度標籤屬性
#為了讓指數標籤有顏色
ax2.tick_params(axis='y', labelcolor='tab:blue')


# 設置x軸界線
plt.xlim(left=0,right=final_alldata.iloc[-1,0])
# 設置x軸軸標籤
plt.xticks(np.arange(0, len(final_alldata), 10), final_alldata['yearQ'][::10])


# 添加格線
ax1.grid(True)
plt.title('利率 vs 全國住宅房價指數')
#bbox_inches將多餘的邊緣空白部分刪除，讓圖片更加緊湊
plt.savefig('利率 vs 全國住宅房價指數.png', dpi=1200, bbox_inches='tight')

plt.show()

#資料庫關閉
con.close() 