import json
import os
from gensim.models import Word2Vec
from tqdm import tqdm

directory = 'states'

for file in tqdm(os.listdir(directory)):
    with open(os.path.join(directory,file)) as f:
        d = json.load(f)
    
    state_text = [sent.strip().split() for x in d for sent in x['full_text'].split(".")]
    model = Word2Vec(sentences = state_text, min_count = 50, sg = 1, negative = 5, ns_exponent = 0.75)
    # add additional models

    model.save("word2vec_models/"+file[:2]+"_word2vec.model")