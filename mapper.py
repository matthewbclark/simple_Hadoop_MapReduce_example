#!/usr/bin/env python
import sys, string
from sklearn.feature_extraction import stop_words

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower case
    line = line.lower()

    # removing punctuation
    line = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    # inserting stopwords
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stops:
		print '%s\t%s' % (word, "1")
