import nltk
import os
from nltk.util import ngrams

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')


character_counter = dict()

books = list([1, 2, 3, 4, 5, 6, 7])
print '{},{},{},{},{},{},{},{},{},{}'.format(
    'Expecto Patronum',
    'Accio',
    'Wingardium Leviosa',
    'Expelliarmus',
    'Stupefy',
    'Lumos',
    'Alohomora',
    'Imperio',
    'Crucio',
    'Avada Kedavra',
)
for i in books:
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" %
                             (str(i)))).read().lower()
    print '{},{},{},{},{},{},{},{},{},{}'.format(
        book.count('expecto patronum'),
        book.count('accio'),
        book.count('wingardium leviosa'),
        book.count('expelliarmus'),
        book.count('stupefy'),
        book.count('lumos'),
        book.count('alohomora'),
        book.count('imperio'),
        book.count('crucio'),
        book.count('avada kedavra')
    )
