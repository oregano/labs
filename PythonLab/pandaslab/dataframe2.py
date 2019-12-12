# Import pandas library
import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

# print dataframe.
# print(df)

# add index

df = pd.DataFrame(data, columns=['Name', 'Age'], index=[
                  'ID1', 'ID2', 'ID3'])

# print dataframe with indexes

print('data-frame')
print(df)

# print with iloc

# print(df.iloc[1][1])

# print with loc

# print(df.loc['ID3']['Age'])

# print with at

# print(df.at['ID1', 'Age'])

# print with iAt

# print(df.iat[0, 1])

# print with 'loc'

# print(df.loc[:, 'Name'])

# print(df.loc['ID2',:])

# add rows in dataframes

df.loc['ID4'] = ['raj', 26]

# modify rows

df.loc['ID2', 'Name'] = ['kaifee']

print(df)

# copying columns

df['Marks'] = df['Age']

print(df)

# perform operation

df['Marks'] += 2

print(df)

print('max')
print(df.max())
