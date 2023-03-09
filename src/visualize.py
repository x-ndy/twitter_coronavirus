#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

freq = []
hashtag = []

for k,v in items:
    hashtag.append(k)
    freq.append(v)
data = pd.DataFrame(
        {'Hashtag': hashtag,'Frequency': freq}
        )
data = data.sort_values('Frequency', ascending = True).tail(10)
data.plot(x = 'Hashtag', y = 'Frequency', kind = 'bar')
plt.xlabel('')
plt.ylabel('')
plt.savefig(f"{args.key}country.png")











