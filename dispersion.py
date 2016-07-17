import nltk
import os
import json

character_counter = dict()

books = list([1, 2, 3, 4, 5, 6, 7])
entire_text = ''
for i in books:
    print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    entire_text += book

tokens = nltk.word_tokenize(entire_text.decode('utf-8'))
mytext = nltk.Text(tokens)
words = [
    "Sirius", "Viktor", "Cedric", "Rita",
    "Bellatrix", "Tonks", "Dobby", "Dudley", "Cho"
]
nltk.draw.dispersion.dispersion_plot(
    mytext, words, ignore_case=False,
    title='Word Dispersion in the Harry Potter Series'
)
