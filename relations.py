import nltk
import os
import copy

character_counter = dict()
list_of_slices = set()
adding_to_slices = []
rolling_words = []

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

        for word_slice in adding_to_slices:
            if len(word_slice) == 100:
                list_of_slices.add(tuple(word_slice))
            else:
                word_slice.append(word)

        if len(rolling_words) < 50:
            rolling_words.append(word)
        else:
            rolling_words.pop(0)
            rolling_words.append(word)

        if 'Harry' in word:
            word_slice = []
            word_slice = rolling_words + ['Harry']
            adding_to_slices.append(word_slice)


print list_of_slices
