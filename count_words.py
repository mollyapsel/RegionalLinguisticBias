import json
import os
from tqdm import tqdm

directory = 'states'
state_ct = {}

for file in tqdm(os.listdir(directory)):
    with open(os.path.join(directory,file)) as f:
        d = json.load(f)
    ct = 0
    for x in d:
        ct += len([word for word in x['full_text'].split() if word != "."])
    state_ct[file[:2]] = ct

print(state_ct)