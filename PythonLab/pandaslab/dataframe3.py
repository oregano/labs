import pandas as pd
import numpy as np

data = np.ones([3, 3], dtype=int)

df = pd.DataFrame(data, columns=['Num1', 'Num2', 'Num3'])

# data frames - all ones
print(df)

df['Num2'] += 1
df['Num3'] += 2

print(df)

# use map

df = map(lambda x: x + 1, df)

print(df)
