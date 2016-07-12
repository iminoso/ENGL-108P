import nltk
import os
from nltk.util import ngrams

character_counter = dict()

# books = list([1, 2, 3, 4, 5, 6, 7])
books = [1]
for i in books:
    print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    # book.dispersion_plot(["Harry", "Voldemort"])
    tokens = nltk.word_tokenize(book.decode('utf-8', 'ignore'))
    # tokens = nltk.word_tokenize(book.decode('utf-8'))
    str_bigrams = ngrams(tokens, 3)
    for gram in str_bigrams:
        print str(gram[0].encode('utf-8'))
        # if gram[0].lower() == 'ron' and gram[0].lower() == 'and' and gram[2].lower() == 'hermione':
        #     print '<<<<<<<<<<<<<<<'
