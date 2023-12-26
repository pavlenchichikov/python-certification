import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

unique_values = list(set(lst))
one_hot_encoded = []

for value in lst:
    encoding = [1 if value == unique_value else 0 for unique_value in unique_values]
    one_hot_encoded.append(encoding)

data = pd.DataFrame(one_hot_encoded, columns=unique_values)
data.head()