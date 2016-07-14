import nltk
import os
from nltk.util import ngrams


character_counter = dict()

# books = list([1, 2, 3, 4, 5, 6, 7])
count = 0
books = [1]
for i in books:
    print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()

    tokens = nltk.word_tokenize(book.decode('utf-8', 'ignore'))

    for t in tokens:
        print t

    # str_bigrams = ngrams(tokens, 3)
    # ctr = 0
    # for gram in str_bigrams:
    #     ctr += 1
    #     g = [str(x.encode('utf-8')) for x in gram]
    #     if "Ron" in g and "Hermione" in g:
    #         print g, gram, ctr
    #         count += 1
print count
