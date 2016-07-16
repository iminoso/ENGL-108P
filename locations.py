import nltk
import os
from nltk.util import ngrams

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')


character_counter = dict()

books = list([1, 2, 3, 4, 5, 6, 7])
for i in books:
    # print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read().lower()
    print book.count('privet drive'), book.count('diagon alley'), book.count('hogwarts'), book.count('azkaban'), book.count('ministry of magic'), book.count('grimmauld place')
