import pandas as pd
import sqlite3
#讀取csv資料集檔案
data_interest_rate=pd.read_csv('debit_interest_finally.csv',encoding=('ANSI'))
data_real_estate_index=pd.read_csv('real_state_index.csv',encoding=('ANSI'))
data_gdp=pd.read_csv('newgdp.csv',encoding=('ANSI'))
data_pop=pd.read_csv('pop.csv',encoding=('ANSI')).T
data_pop=data_pop.reset_index()
# 將第一筆資料設為欄名
data_pop.columns = data_pop.iloc[0]
# 刪除第一筆資料
data_pop = data_pop.drop(0)
data_debit_interest=pd.read_csv('debit&interest.csv',encoding=('ANSI'))

#建立資料庫
conn=sqlite3.connect('f_crisis.db')

#建立資料表
conn.execute('''CREATE TABLE IF NOT EXISTS interest_rate(time text,interest float) ''')
conn.execute('''CREATE TABLE IF NOT EXISTS real_estate_index(yearQ text,TW float,TPE float,NTP float,Taoyuan float,\
             Hsinchu float,Taichung float,Tainan float) ''')
conn.execute('''CREATE TABLE IF NOT EXISTS GDP(year TEXT,exchange_rate FLOAT,YOY FLOAT,GDP_millionUSD INT,\
             per_GDP INT,GNI_millionUSD INT,per_GNI INT,NI_millionUSD INT,per_NI INT) ''')
    
conn.execute('''CREATE TABLE IF NOT EXISTS pop(year text,young_person_pop int)''')
conn.execute('''CREATE TABLE IF NOT EXISTS debit_interest(year text,debit int,interest float)''')

for i in range(len(data_interest_rate)):
    sql_interest_rate =''' insert into interest_rate(time,interest) values('{}',{})'''
    sql_interest_rate=sql_interest_rate.format(data_interest_rate.iloc[i,0],data_interest_rate.iloc[i,1])
    # print(sql_interest_rate)
    #執行sql指令
    cur=conn.execute(sql_interest_rate) 
   
for j in range(len(data_real_estate_index)):
    sql_real_estate_index =''' insert into real_estate_index(yearQ,TW,TPE,NTP,Taoyuan,Hsinchu,Taichung,Tainan) 
    values('{}',{},{},{},{},{},{},{})'''
    sql_real_estate_index=sql_real_estate_index.format(data_real_estate_index.iloc[j,0],data_real_estate_index.iloc[j,1],\
                                                       data_real_estate_index.iloc[j,2],data_real_estate_index.iloc[j,3],\
                                                           data_real_estate_index.iloc[j,4],data_real_estate_index.iloc[j,5],\
                                                               data_real_estate_index.iloc[j,6],data_real_estate_index.iloc[j,7])
    # print(sql_real_estate_index)
    #執行sql指令
    cur=conn.execute(sql_real_estate_index)
  
for k in range(len(data_gdp)):
    sql_gdp =''' insert into GDP(year,exchange_rate,YOY,GDP_millionUSD,per_GDP,GNI_millionUSD,per_GNI, \
              NI_millionUSD,per_NI) values('{}',{},{},{},{},{},{},{},{})'''
    sql_gdp=sql_gdp.format(data_gdp.iloc[k,0],data_gdp.iloc[k,1],\
                           data_gdp.iloc[k,2],data_gdp.iloc[k,3],\
                           data_gdp.iloc[k,4],data_gdp.iloc[k,5],\
                           data_gdp.iloc[k,6],data_gdp.iloc[k,7],\
                           data_gdp.iloc[k,8])
    # print(sql_gdp)
    #執行sql指令
    cur=conn.execute(sql_gdp)
for a in range(len(data_pop)):
    sql_pop =''' insert into pop(year,young_person_pop) values('{}',{})'''
    sql_pop=sql_pop.format(data_pop.iloc[a,0],data_pop.iloc[a,2])
    # print(sql_pop)
    #執行sql指令
    cur=conn.execute(sql_pop) 
for b in range(len(data_debit_interest)):
    sql_debit_interest='''insert into debit_interest(year ,debit ,interest ) values('{}',{},{})'''
    sql_debit_interest=sql_debit_interest.format(data_debit_interest.iloc[b,0],data_debit_interest.iloc[b,-2],data_debit_interest.iloc[b,-1])
    # print(sql_debit_interest)
    cur=conn.execute(sql_debit_interest) 
conn.commit()
conn.close()  

    

#%%
#如果資料表存在，就寫入資料,否則建立資料表
# data_interest_rate.to_sql('interest_rate', conn,if_exists='replace',index=False)
# data_real_estate_index.to_sql('real_estate_index', conn,if_exists='replace',index=False)
# data_gdp.to_sql('GDP', conn,if_exists='replace',index=False)
