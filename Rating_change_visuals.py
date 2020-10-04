import pandas as pd
import numpy as np

df = pd.read_json('https://codeforces.com/api/user.ratedList?activeOnly=true')
result = pd.DataFrame.from_records(df['result'])
result['registrationTimeSeconds'] = pd.to_datetime(result['registrationTimeSeconds'],unit='s').dt.date

result

from matplotlib import pyplot as plt

plt.subplots(figsize=(17, 7))
plt.style.use('seaborn')

color_dict = dict({'newbie':'grey',
                  'pupil':'green',
                  'specialist': 'cyan',
                  'expert': 'blue',
                  'candidate master': 'purple',
                   'master': 'orange',
                   'international master': 'orange',
                   'grandmaster': 'red',
                   'international grandmaster': 'red',
                   'legendary grandmaster': 'black'})

for group, frame in result.groupby('rank'):
  colour = color_dict[group]
  plt.scatter(frame['registrationTimeSeconds'], frame['rating'], c=colour, s=10, alpha=0.5)

plt.xlabel('Registration Time')
plt.ylabel('Rating')
plt.title('Rating vs Registration time')
plt.tight_layout()
#plt.savefig('Rating_wrt_registration_time.png')
plt.show()

from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ranks = []
coders = []
colours = []
for group, frame in result.groupby('rank'):
  ranks.append(group)
  coders.append(len(frame))
  colours.append(color_dict[group])

print(ranks)
# print(coders)

plt.pie(coders, colors=colours, explode=[0.1, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0], wedgeprops={'edgecolor': 'black'})

plt.title("Division of ranks")
plt.tight_layout()
plt.show()

from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

rating_dict = dict({'newbie':1000,
                  'pupil':1300,
                  'specialist': 1500,
                  'expert': 1750,
                  'candidate master': 2000,
                   'master': 2200,
                   'international master': 2350,
                   'grandmaster': 2500,
                   'international grandmaster': 2800,
                   'legendary grandmaster': 3300})

for group, frame in result.groupby('country'):
  if group != 'Russia' and group != 'Japan' and group != 'China' and group != 'India':
    continue
  
  rating = []
  coders = []
  ex = []
  
  for g, f in frame.groupby('rank'):
    ex.append([rating_dict[g], len(f)])

  ex.sort()
  for i in ex:
    rating.append(i[0])
    coders.append(i[1])
  
  plt.plot(rating, coders, label=group)

plt.yscale('log')
plt.title('Codeforces div 1 stats')
plt.xlabel('Rating Range')
plt.ylabel('Number of coders')

plt.legend()
plt.tight_layout()
plt.savefig('Codeforces_stats.png')
plt.show()
