import nltk
import os
import json

character_counter = dict()

# books = list([1, 2, 3, 4, 5, 6, 7])
books = [7]
for i in books:
    print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    # book.dispersion_plot(["Harry", "Voldemort"])
    tokens = nltk.word_tokenize(book.decode('utf-8'))
    mytext = nltk.Text(tokens)
    mytext.dispersion_plot(["Harry", "Ron", "Hermione", "Malfoy", "Dumbledore", "Voldemort"])
