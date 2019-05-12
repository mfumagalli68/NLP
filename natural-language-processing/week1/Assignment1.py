import sys
sys.path.append("/home/marco/CourseraNLP/natural-language-processing")
import pandas as pd
import numpy as np
import os
from ast import literal_eval
import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords

def read_data(path_file,test=False):


    if test:
        data = pd.read_csv(path_file, sep='\t')
        return (data)

    else:

        data = pd.read_csv(path_file,sep='\t')
        data['tags'] = data['tags'].apply(literal_eval)

        return (data)



train = read_data('data/train.tsv')
test = read_data('data/test.tsv',test=True)

print (train.head())
