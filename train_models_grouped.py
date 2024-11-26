import json
import os
from gensim.models import Word2Vec
from gensim.models import FastText
from tqdm import tqdm

directory = 'states'
regions = {1: ['WA', 'OR', 'CA', 'AK', 'HI'], 2: ['AZ', 'NM', 'TX', 'NV', 'UT'], 3: ['MT', 'WY', 'CO', 'ID'], 4: ['ND', 'SD', 'NE', 'KS', 'OK', 'MO', 'IA'], 5: ['MN', 'WI', 'IL', 'MI', 'OH'], 6: ['MS', 'LA', 'AL', 'GA', 'FL', 'SC', 'KY', 'TN', 'AR', 'IN', 'WV'], 7: ['NY', 'NJ', 'PA'], 8: ['ME', 'NH', 'VT', 'MA', 'RI', 'CT'], 9:['VA','DC','MD','DE','NC']}

for r in tqdm(regions.keys()): 
    combined_corp = []
    for state in regions[r]:
        with open(os.path.join(directory, state+'.json')) as f:
            d = json.load(f)
        combined_corp += [sent.strip().split() for x in d for sent in x['full_text'].split(".")]
   
    print("region "+ str(r)+ ": "+ str(len(combined_corp)) + " tokens")
    # word2vec
    # model2 = Word2Vec(sentences = combined_corp, min_count = 2, sg = 1, negative = 5, ns_exponent = 0.75)
    # model5 = Word2Vec(sentences = combined_corp, min_count = 5, sg = 1, negative = 5, ns_exponent = 0.75)

    # model2.save("w2v_regions-mc2/r"+str(r)+"_word2vec-mc2.model")
    # model5.save("w2v_regions-mc5/r"+str(r)+"_word2vec-mc5.model")

    # fastText
    model = FastText(sentences = combined_corp, min_count = 2, sg = 1, negative = 5, ns_exponent = 0.75)
    model.save("ft_regions/r"+str(r)+"_ft.model")