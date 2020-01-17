import pandas as pd
import numpy as np

# create a series

sr = pd.Series([1, 4, 3, 5, 2, 8, 7, 6], dtype='int32')

print(sr)

# creating a series with heterogeneous data(it won't fail but the data type would be object)

sr = pd.Series([1, 3, 'a string', 4.4])

print(sr)

# create a data frame with randome numbers

dates = pd.date_range('20190101', periods=7, freq='D')

print(dates)

df = pd.DataFrame(np.random.randn(7, 5), index=dates, columns=list('ABCDE'))

print(df)

# querying only top 3 rows from data frame

print(df.head(3))

# querying only bottom 2 rows from data frame

print(df.tail(2))

# use of describe
print(df.describe())

# set a flag

df['F'] = df['C'] > 1

print(df)

# boolean masking
print(df[df['A'] > 0])
print(df[(df['A'] > 0) | (df['B'] > 0)])
print(df[(df['A'] > 0) & (df['B'] > 0)])
