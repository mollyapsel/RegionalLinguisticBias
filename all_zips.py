import json
import pandas as pd
import os
from tqdm import tqdm

directory = 'states'

zips = set()
for file in tqdm(os.listdir(directory)):
    with open(os.path.join(directory,file)) as f:
        d = json.load(f)

    for x in d:
        zips.add(x['zip_code'])

data = {'Zip': list(zips)}
pd.DataFrame(data).to_csv('zips.csv', index=False)