import numpy as np
import pandas as pd

####Dataset 
Population = pd.read_excel("C:\\Users\\USER\\Desktop\\data science\\Case_Interview\\task.xlsx",'whole_population')
sample = pd.read_excel("C:\\Users\\USER\\Desktop\\data science\\Case_Interview\\task.xlsx",'data_to_sample')

Population.head()
sample.head()

print('Total number of rows is {} and columns is {}'.format(Population.shape[0], Population.shape[1]))
Population.isnull().sum()
Population.isna().sum()
sample.isnull().sum()
sample.isna().sum()
##We have 3 colums which is having null values 
#gonna remove all the irrelavant column which might not be 
#useful for our analysis 
columns_to_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']
#drop the irrelevant columns
df_population = Population.drop(columns = columns_to_drop)
df_sample = sample.drop(columns = columns_to_drop)
df_population.head()
df_sample.head()
print('Total number of rows is {} and columns is {}'.format(df_population.shape[0], df_population.shape[1]))
###Lets find the total number favourite fruit and their listing
group1 =len(df_population['favourite_fruit'].unique())
group2 =len(df_sample['favourite_fruit'].unique())
###It will show no null value and na value
#Now lets look into number of categorical variables and numerical variables.
cat_df = df_population.select_dtypes(include=['object'])
print('There are {} categorical variables in our dataset'.format(cat_df.shape[1]))
####Now we have to find the two data frames population and sample we need to find the in population what all present
##in sample.
df = pd.concat([df_population, df_sample])
df = df.reset_index(drop=True)
df_gpby = df.groupby(list(df.columns))
idx = [x[0] for x in df_gpby.groups.values() if len(x) != 1]
df.reindex(idx)
final = df.reindex(idx)
final
###Above is the output which we will cpy in CSV or excel format and provide the datasets
# determining the name of the file
file_name = 'output_q5.xlsx'
# saving the excel
final.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')







