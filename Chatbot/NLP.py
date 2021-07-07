#### Importamos librerias
import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()



#### La tokenizacion separa las oraciones en palabras (tokens), toma por separado palabras/numeros/caracteres
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

#### El stemming lleva la palabra a su forma original (Inscripcion == Inscribir)
def stem(word):
    return stemmer.stem(word.lower())

#### BoW nos devuelve la cantidad de veces que utilizamos cada palabra del input en comparacion a la data (en un array numerico= 1,0,1,1 por ejemplo)
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag