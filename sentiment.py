import nltk
import os
from pattern.en import sentiment
import unicodedata
import json


character_counter = dict()

books = list([1, 2, 3, 4, 5, 6, 7])
# entire_text = ''
# books = [2]
book_names = [
    'Philosopher\'s Stone',
    'Chamber of Secrets',
    'Prisoner of Azkaban',
    'Goblet of Fire',
    'Order of the Phoenix',
    'Half-Blood Prince',
    'Deathly Hallows'
]
for i in books:
    book_name = "book_%s.txt" % (str(i))
    book = open(os.path.join('dataset', "book_%s.txt" % (str(i)))).read()
    # entire_text += book

    most_neg = 1
    most_neg_sent = []
    sent_tokens = nltk.sent_tokenize(book.decode('utf-8'))
    count = {'pos': 0, 'neg': 0, 'neut': 0}
    for index, s in enumerate(sent_tokens):
        sentence = unicodedata.normalize('NFKD', s).encode(
            'ascii', 'ignore').replace('\n\n', ' ')
        polarity, subjectivity = sentiment(sentence)

        if polarity > 0:
            count['pos'] += 1
        elif polarity < 0:
            count['neg'] += 1
        else:
            count['neut'] += 1

        if polarity < most_neg:
            most_neg = polarity
            most_neg_sent = [(sentence, polarity, subjectivity)]
        elif polarity == most_neg:
            most_neg_sent.append((sentence, polarity, subjectivity))
    print json.dumps(
        most_neg_sent, sort_keys=True, indent=2
    )
    print "{},{},{},{}".format(
        book_names[i - 1],
        (count['neut'] / float(len(sent_tokens))),
        (count['pos'] / float(len(sent_tokens))),
        (count['neg'] / float(len(sent_tokens)))
    )
