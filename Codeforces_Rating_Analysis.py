import pandas as pd
import numpy as np

df = pd.read_json('https://codeforces.com/api/user.ratedList?activeOnly=true')
result = pd.DataFrame.from_records(df['result'])

result


# Total number of active indian masters or above
hello = result
country = 'India'

LGM = len(hello[(hello['rating'] >= 3000) & (hello['country'] == country)])
IGM = len(hello[(hello['rating'] >= 2600) & (hello['country'] == country)]) - LGM
GM = len(hello[(hello['rating'] >= 2400) & (hello['country'] == country)]) - LGM - IGM
IM = len(hello[(hello['rating'] >= 2300) & (hello['country'] == country)]) - GM - LGM - IGM
M = len(hello[(hello['rating'] >= 2100) & (hello['country'] == country)]) - GM - LGM - IGM - IM
CM = len(hello[(hello['rating'] >= 1900) & (hello['country'] == country)]) - GM - LGM - IGM - IM - M

print(country, '->', 'LGM', LGM)
print(country, '->', 'IGM', IGM)
print(country, '->', 'GM', GM)
print(country, '->', 'IM', IM)
print(country, '->', 'M', M)
print(country, '->', 'CM', CM)

# print('Indian masters and above', len(hello[(hello['rating'] >= 2100) & (hello['country'] == 'India')]))
# print('Indian Grandmasters and above', len(hello[(hello['rating'] >= 2400) & (hello['country'] == 'India')]))
# print('Indian masters and above', len(hello[(hello['rating'] >= 2100) & (hello['country'] == 'India')]))
