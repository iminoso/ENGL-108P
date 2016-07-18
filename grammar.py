import nltk
import os
from pattern.en import sentiment
import unicodedata
import json

books = list([1, 2, 3, 4, 5, 6, 7])

# books = [1, 2, 3, 4]
book_names = [
    'Philosopher\'s Stone',
    'Chamber of Secrets',
    'Prisoner of Azkaban',
    'Goblet of Fire',
    'Order of the Phoenix',
    'Half-Blood Prince',
    'Deathly Hallows'
]
count = {}
pos_type = 'VB'
for i in books:
    book_name = "book_%s.txt" % (str(i))
    print book_name
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    book = book.lower()
    words_tokens = nltk.word_tokenize(book.decode('utf-8'))
    pos_text = nltk.pos_tag(words_tokens)
    for word in nltk.pos_tag(words_tokens):
        text, text_type = word
        # decode
        text = unicodedata.normalize('NFKD', text).encode(
            'ascii', 'ignore').replace('\n\n', ' ')
        if text in count and text_type == pos_type:
            count[text] += 1
        else:
            count[text] = 1

print sorted(count.items(), key=lambda item: item[1])

# print json.dumps(
#     most_neg_sent, sort_keys=True, indent=2
# )
# print "{},{},{},{}".format(
#     book_names[i - 1],
#     (count['neut'] / float(len(sent_tokens))),
#     (count['pos'] / float(len(sent_tokens))),
#     (count['neg'] / float(len(sent_tokens)))
# )
