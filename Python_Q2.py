import numpy as np
import pandas as pd

####Dataset 
df = pd.read_excel("C:\\Users\\USER\\Desktop\\data science\\Case_Interview\\task3.xlsx")
##Adding new column in dataframe for month from timestamp

df['month'] = pd.DatetimeIndex(df['order_date']).month
#df

###Order_date Sorting 
df1 = df.sort_values(by='order_date')

#Create a DataFrame object

provider=df['provider']
order_count=df['order_count']
date=df['order_date']
revenue=df['revenue']

###split the data frame into months, Product
uniqueValues = df1['product'].unique()
uniqueValues_month = df1['month'].unique()
df2= df1.groupby(['month'])

#print("uniqueValues is",uniqueValues)
#print(len(uniqueValues_month))
dict_rr_month=dict.fromkeys(uniqueValues_month,0)
df1_splitmonth = df1
for m in uniqueValues_month: 
    dict_rr_comm=dict.fromkeys(uniqueValues,0)
    dict_rr_gross=dict.fromkeys(uniqueValues,0)
    dict_dd_comm=dict.fromkeys(uniqueValues,0)
    dict_dd_gross=dict.fromkeys(uniqueValues,0)
    dict_mm_comm=dict.fromkeys(uniqueValues,0)
    dict_mm_gross=dict.fromkeys(uniqueValues,0)
    dict_tj_comm=dict.fromkeys(uniqueValues,0)
    dict_tj_gross=dict.fromkeys(uniqueValues,0)
    dict_tj_revn=dict.fromkeys(uniqueValues,0)
   
    mm_ordercnt=0
    mm_comm=0
    mm_revenue=0
    #df1 = df1[df1['month'] == m]   
    for prod in uniqueValues:
        for index, row in df1.iterrows():
            if row['month'] == m:
                if row['product'] == prod:
                    if row['provider'] == 'roadrunner':
                        dict_rr_comm[prod]  += (50 * row['order_count'])
                        dict_rr_gross[prod] += row['revenue']-(50 * row['order_count'])
                        #dict_rr_month[month]=[dict_rr_comm[prod],dict_rr_gross[prod]]
                    elif row['provider'] == 'donald_duck':
                        dict_dd_comm[prod]  += (50 * row['order_count'])
                        dict_dd_gross[prod] += row['revenue']-(50 * row['order_count'])
                    elif row['provider'] == 'tom_jerry':
                        dict_tj_revn[prod]  += row['revenue']
                    elif row['provider'] == 'micky_mouse':
                        mm_ordercnt  += row['order_count']
                        if mm_ordercnt <= 500:
                           mm_comm = 10000
                        elif mm_ordercnt > 500:
                           mm_comm=0
                           mm_comm += (10000 +(10 * row['order_count']))
                        mm_revenue += row['revenue']
                           
        
        print('Total Revenue for mickymouse for this month',mm_revenue,'Commision:', mm_comm, 'gross:',mm_revenue-mm_comm )
        
        print('Total Comission for Roadrunner for this month',m,'for product',prod,'is',dict_rr_comm[prod])
        print('Total Comission for DonalDuck for this month',m,'for product',prod,'is',dict_dd_comm[prod])
        print('Total Revenue for TomJerry for this month',m,'for product',prod,'is',dict_tj_revn[prod])
        dict_tj_gross[prod]=dict_tj_revn[prod]-2000
        print('Total Gross for TomJerry for this month',m,'for product',prod,'is',dict_tj_revn[prod]-2000)

    print("RoadRunner monthly commission dictionary",dict_rr_comm)
    print("RoadRunner monthly Gross dictionary",dict_rr_gross)
    print("DonalDuck monthly commission dictionary",dict_dd_comm)
    print("DonalDuck monthly Gross dictionary",dict_dd_gross)
    print("TomJerry monthly Gross dictionary",dict_tj_gross)

