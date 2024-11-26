import json
import os
from gensim.models import Word2Vec
from tqdm import tqdm
import pandas as pd

directory = 'states'
pol = pd.read_csv('zips_geocodio_7200535c0de6cfe010bb3e5fa4c8ce0520b61862.csv')
rep_text = []
dem_text = []
ind_text = []

for file in tqdm(os.listdir(directory)):
    with open(os.path.join(directory,file)) as f:
        d = json.load(f)

    for x in d:
        z = int(x['zip_code'])
        party = pol.loc[pol['Zip']==z, 'Current Representative Party'].iloc[0]
        if party=='Republican':
            rep_text += [sent.strip().split() for sent in x['full_text'].split(".")]
        elif party=='Democrat':
            dem_text += [sent.strip().split() for sent in x['full_text'].split(".")]
        elif party=='Independent':
            ind_text += [sent.strip().split() for sent in x['full_text'].split(".")]
        
print("Republican tokens:", len(rep_text))
rmodel = Word2Vec(sentences = rep_text, min_count = 2, sg = 1, negative = 5, ns_exponent = 0.75)
rmodel.save("w2v_polparty/rep_word2vec2.model")
print("Democrat tokens:", len(dem_text))
dmodel = Word2Vec(sentences = dem_text, min_count = 2, sg = 1, negative = 5, ns_exponent = 0.75)
dmodel.save("w2v_polparty/dem_word2vec2.model")

# add additional models

