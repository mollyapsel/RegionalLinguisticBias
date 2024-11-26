import json
import pandas as pd
from uszipcode import SearchEngine
import os
from tqdm import tqdm

sources = pd.read_csv('merged_output.csv')
sources.loc[sources['zip_code'] == 7520, 'zip_code'] = 75201
sources.loc[sources['zip_code'] == 1809, 'zip_code'] = 18042

search = SearchEngine()
state_collections = {}
directory = 'Clean_text' 

for file in tqdm(os.listdir(directory)):
  with open(os.path.join(directory,file)) as f:
      d = json.load(f)
      #print(d)

  for x in d:
    id = int(x['text_id'])
    if id in sources['ID'].values:
      # get the value of the zip_code column in the row with the matching ID
      zip_code = sources.loc[sources['ID'] == id, 'zip_code'].iloc[0]
      # if zip_code is not NaN
      if pd.isna(zip_code):
        continue
      zip_code = int(zip_code)
      if search.by_zipcode(zip_code) is None:
        for i in range(10):
          if search.by_zipcode(str(zip_code) + str(i)) is not None:
            zip_code = str(zip_code) + str(i)
            break
        else:
          continue

      x['zip_code'] = zip_code
      state = search.by_zipcode(zip_code).state
      if state in state_collections:
        state_collections[state].append(x)
      else:
        state_collections[state] = [x]

for state in state_collections:
  with open('states/'+ state + '.json', 'w') as f:
    json.dump(state_collections[state], f)


