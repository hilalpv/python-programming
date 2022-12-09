# 1.	Write a Python program to Extract Unique values from dictionary values?
dict_1 = {'aditi': 2, 'Kenny': 2, 'Ankita': 3, 'Ricky': 4}
uniqueValues = set(dict_1.values())
print(uniqueValues)

# 2. Write a Python program to find the sum of all items in a dictionary?
scores = {'Anil': 72, 'Kohli': 45, 'Sehwag': 20, 'Dhoni': 50, 'Rishab': 30}
new_Values = sum(scores.values())
print(new_Values)

# 3. Write a Python program to Merging two Dictionaries?
y = dict_1.update(scores)
print(dict_1)

# 4. Write a Python program to convert key-values list to flat dictionary?
import pandas as pd

dict_2 = {'a': 1,
          'c': {'a': 2, 'b': {'x': 5, 'y': 10}},
          'd': [1, 2, 3]}
df = pd.json_normalize(dict_2, sep='-')
print(df.to_dict(orient='records')[0])

# 5. Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])
dict3 = OrderedDict(list(dict1.items()) + list(dict2.items()))

print(dict3)

# 6. Write a Python program to check order of character in string using OrderedDict()?
s = "balloon"
order = "lno"


def check_pattern(s):
    od = OrderedDict.fromkeys(s)
    x = 0
    for i in od.keys():
        if i == order[x]:
            x = x + 1
        if x == len(order):
            return True
    return False


print(check_pattern(s))


# 7. Write a Python program to sort Python Dictionaries by Key or Value?

def Sort_valuekeys(dict_1):
    for keys in dict_1.keys():
        x = OrderedDict(sorted(dict_1.items()))
        return x
scores = {'Anil': 72, 'Kohli': 45, 'Sehwag': 20, 'Dhoni': 50, 'Rishab': 30}

print(Sort_valuekeys(scores))
