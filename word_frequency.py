#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
from collections import OrderedDict
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="the file you want to analyse")
parser.add_argument("--min_word_frequency", help="the minimum word frequency that you want to show", type=int)
parser.add_argument("--stop_words", help="stop words you wish to exclude")

args = parser.parse_args()

my_file = Path(args.file)
if not my_file.is_file():
    sys.exit("Error: file does not exist!")

if args.min_word_frequency is None:
    min_word_frequency = 0
else:
    min_word_frequency = args.min_word_frequency

if args.stop_words:
    stop_word_list = args.stop_words.split()
else:
    stop_word_list = list()

word_dict = {}

with open(my_file,'r') as f:
    for line in f:
        for word in line.split():
            if word_dict.get(word):
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict.update({word:1})

sorted_word_dict = OrderedDict(sorted(word_dict.items(), key = itemgetter(1), reverse = True))

print("\n :: Word Frequency Analyser ::\n")

for word in sorted_word_dict:
    frequency = sorted_word_dict[word]
    if frequency >= min_word_frequency and word not in stop_word_list:
        print("{}: {}".format(word, sorted_word_dict[word]))