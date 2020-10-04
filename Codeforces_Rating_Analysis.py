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

# bar graph to visulize Rating distribution

divide_into = []
for i in range(0, 3500, 50):
  divide_into.append(i)

rating_condition = (result['rating'] >= 0)
ratings = result[rating_condition]
ratings = ratings['rating']

fig, ax = plt.subplots(figsize=(20, 10))

n, bins, patches = ax.hist(ratings, divide_into, edgecolor='black')

ax.set_xlabel('Rating range')
ax.set_ylabel('Number of coders')
ax.set_title('Rating distribution')

for i in range(0, len(patches)):
  if i < 24:
    patches[i].set_facecolor('grey') # Newbie
  elif i < 28:
    patches[i].set_facecolor('#008000') # Pupil
  elif i < 32:
    patches[i].set_facecolor('#32a89e') # Specialist
  elif i < 38:
    patches[i].set_facecolor('#0000ff')  # Expert
  elif i < 42:
    patches[i].set_facecolor('#aa00aa') # Candidate Master
  elif i < 48:
    patches[i].set_facecolor('orange') # Master and International master
  else:
    patches[i].set_facecolor('red') # Grand Master and family

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
