import pandas as pd
import numpy as np

df = pd.read_json('https://codeforces.com/api/contest.ratingChanges?contestId=1406')
result = pd.DataFrame.from_records(df['result'])

result['delta'] = (result['newRating'] - result['oldRating'])
result

from matplotlib import pyplot as plt

plt.style.use('seaborn')
plt.subplots(figsize=(17, 7))

color_dict = dict({'Newbie':'grey',
                  'Pupil':'green',
                  'Specialist': 'cyan',
                  'Expert': 'blue',
                   'Candidate Master': 'purple'})

plt.scatter(result['rank'], result['delta'], c=result['oldRating'], cmap='rainbow', s=10)

cbar = plt.colorbar()
cbar.set_label('Rating')

plt.tight_layout()
plt.show()

from matplotlib import pyplot as plt

use = result
plt.style.use('seaborn')
plt.subplots(figsize=(17, 7))

tem = use[use['oldRating'] < 1200]
plt.scatter(tem['rank'], tem['delta'], s=10, c='gray')

tem = use[(use['oldRating'] < 1400)&(use['oldRating'] >= 1200)]
plt.scatter(tem['rank'], tem['delta'], s=10, c='#00802e')

tem = use[(use['oldRating'] < 1600)&(use['oldRating'] >= 1400)]
plt.scatter(tem['rank'], tem['delta'], s=10, c='#03a8ac')

tem = use[(use['oldRating'] < 1900)&(use['oldRating'] >= 1600)]
plt.scatter(tem['rank'], tem['delta'], s=10, c='#0000ff')

tem = use[(use['oldRating'] < 2100)&(use['oldRating'] >= 1900)]
plt.scatter(tem['rank'], tem['delta'], s=10, c='#aa00b6')

plt.title('Codeforces Round #534 (Div. 2)')
plt.xlabel('Current Rating')
plt.ylabel('Rating change (Delta)')

plt.tight_layout()
# plt.savefig('CF#534.png')
plt.show()
