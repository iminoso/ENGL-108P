import nltk
import os
import copy
import json

character_counter = dict()
list_of_slices = []
adding_to_slices = []
rolling_words = []

output_file = open('outputs/relations.txt', 'w+')

# books = list([1, 2, 3, 4, 5, 6, 7])
books = [1]
ctr = 0
for i in books:
    print 'Book {}'.format(i)
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()

    tokens = nltk.word_tokenize(book.decode('utf-8', 'ignore'))

    for t in tokens:
        word = str(t.encode('utf-8'))

        for i, word_slice in enumerate(adding_to_slices):
            if len(word_slice[0]) == 100:
                if word_slice[1]:
                    list_of_slices.append(word_slice[0])
            else:
                adding_to_slices[i][0].append(word)

        if len(rolling_words) < 50:
            rolling_words.append(word)
        else:
            rolling_words.pop(0)
            rolling_words.append(word)

        if 'Harry' in word:
            word_slice = []
            word_slice = rolling_words + ['Harry']
            adding_to_slices.append([word_slice, True])

print >>output_file, json.dumps(
    list_of_slices, sort_keys=True, indent=2)
