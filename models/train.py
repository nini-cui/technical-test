# Package for data wrangling
import pandas as pd 

# Package for array math
import numpy as np 

# Package for system path traversal
import os

# Package for working with dates
from datetime import date

# K fold analysis package
from sklearn.model_selection import KFold

# Import the main analysis pipeline
from pipeline import Pipeline

# Tensor creation class
from text_preprocessing import TextToTensor

# Reading the configuration file
import yaml
with open("conf.yml", 'r') as file:
    conf = yaml.safe_load(file).get('pipeline')

# Reading the stop words
stop_words = []
try:
    stop_words = pd.read_csv('stop_words.txt', sep='\n', header=None)[0].tolist()
except Exception as e:
    # This exception indicates that the file is missing or is in a bad format
    print('Bad stop_words.txt file: {e}')

# # Reading the data
# train = pd.read_csv('REdata/train.tsv')[['text', 'target']]
# test = pd.read_csv('REdata/test.tsv')

columns = columns = ["sentence", "label"]
train = pd.read_csv('REdata/train.tsv', sep='\t', header=None, names=columns)
test = pd.read_csv('REdata/test.tsv', sep='\t')

# Shuffling the data for the k fold analysis
train = train.sample(frac=1)

# Creating the input for the pipeline
# X_train = train['text'].tolist()
# Y_train = train['target'].tolist()

# X_test = test['text'].tolist()

X_train = train['sentence'].tolist()
Y_train = train['label'].tolist()

X_test = test['sentence'].tolist()
Y_test=test['label'].to_list()


if conf.get('k_fold'):
    kfold = KFold(n_splits=5)
    # acc = []
    # f1 = []
    for train_index, test_index in kfold.split(X_train):
        # Fitting the model and forecasting with a subset of data
        k_results = Pipeline(
            X_train=np.array(X_train)[train_index],
            Y_train=np.array(Y_train)[train_index], 
            embed_path='glove.6B.100d.txt',
            embed_dim=300,
            X_test=np.array(X_train)[test_index],
            Y_test=np.array(Y_train)[test_index],
            max_len=conf.get('max_len'),
            epochs=conf.get('epochs'),
            batch_size=conf.get('batch_size')
        )
        # Saving the accuracy
    #     acc += [k_results.acc]
    #     f1 += [k_results.f1]
    #     print(f'The accuracy score is: {acc[-1]}') 
    #     print(f'The f1 score is: {f1[-1]}') 
    # print(f'Total mean accuracy is: {np.mean(acc)}')
    # print(f'Total mean f1 score is: {np.mean(f1)}')

# Running the pipeline with all the data
results = Pipeline(
    X_train=X_train,
    Y_train=Y_train, 
    embed_path='glove.6B.100d.txt',
    embed_dim=300,
    stop_words=stop_words,
    X_test=X_test,
    max_len=conf.get('max_len'),
    epochs=conf.get('epochs'),
    batch_size=conf.get('batch_size')
)

# Some sanity checks
# good = ["Fire in Vilnius! Where is the fire brigade??? #emergency"]
# bad = ["Sushi or pizza? Life is hard??:(("]

# TextToTensor_instance = TextToTensor(
# tokenizer=results.tokenizer,
# max_len=conf.get('max_len')
# )

# # Converting to tensors
# good_nn = TextToTensor_instance.string_to_tensor(good)
# bad_nn = TextToTensor_instance.string_to_tensor(bad)

# p_good = results.model.predict(good_nn)
# print("p_good prediction result", p_good)


# Forecasting
# p_good = results.model.predict(good_nn)[0][0]
# p_bad = results.model.predict(bad_nn)[0][0]

# print(f'Sentence: {good_nn} Score: {p_good}')
# print(f'Sentence: {bad_nn} Score: {p_bad}')

# # Saving the predictions
# test['prob_is_genuine'] = results.yhat
# test['target'] = [1 if x > 0.5 else 0 for x in results.yhat]
 
# # Saving the predictions to a csv file
# if conf.get('save_results'):
#     if not os.path.isdir('output'):
#         os.mkdir('output')    
#     test[['id', 'target']].to_csv(f'output/submission_{date.today()}.csv', index=False)