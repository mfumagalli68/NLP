import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

def preprocessing(data):

    stopwords = set(stopwords.words('english'))


    data = data.map(lambda x: x.replace(stopwords,''))

d
stopwords= preprocessing(data)
