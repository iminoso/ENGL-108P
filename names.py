import nltk
import os
import json

character_counter = dict()

books = list(1, 2, 3, 4, 5, 6, 7)

for i in books:
    print 'Book {}'.format(i)
    output_file = open('outputs/names_count_book_' + str(i) + '.txt', 'w+')
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    for sentences in nltk.sent_tokenize(book.decode("utf-8")):
        for chunked in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentences))):
            print chunked, chunked[0], type(chunked), len(chunked)
            if type(chunked) is not tuple:
                name = ' '.join(leaf[0] for leaf in chunked.leaves())
                if name in character_counter:
                    character_counter[name] += 1
                else:
                    character_counter[name] = 1
    print >>output_file, json.dumps(
        character_counter, sort_keys=True, indent=2)
