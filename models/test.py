import numpy as np
import pandas as pd
from train import results

from text_preprocessing import TextToTensor

import yaml
with open("conf.yml", 'r') as file:
    conf = yaml.safe_load(file).get('pipeline')

TextToTensor_instance = TextToTensor(
tokenizer=results.tokenizer,
max_len=conf.get('max_len')
)

# test = pd.read_csv('REdata/test.tsv', sep='\t')

test_sentence = ["Our work supported @GENE$ genetic variants as possible susceptibility factors for @DISEASE$ and fractures in humans."]
good_nn = TextToTensor_instance.string_to_tensor(test_sentence)

# good_nn = TextToTensor_instance.string_to_tensor(test["sentence"])

p_good = results.model.predict(good_nn)
prediction_results = np.round(p_good)
print(prediction_results)

