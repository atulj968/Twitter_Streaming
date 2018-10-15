#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:06:54 2018

@author: atuljain
"""

import json
import re
import pandas as pd
import matplotlib.pyplot as plt
tweets_data_path = '/Users/atuljain/Downloads/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
print len(tweets_data)
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

#hastagging
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
tweets['#AbdulKalam'] = tweets['text'].apply(lambda tweet: word_in_text('#AbdulKalam', tweet))
tweets['#kalam'] = tweets['text'].apply(lambda tweet: word_in_text('#kalam', tweet))
tweets['#ApjKalam'] = tweets['text'].apply(lambda tweet: word_in_text('#ApjKalam', tweet))
print tweets['#AbdulKalam'].value_counts()[True]
print tweets['#kalam'].value_counts()[True]
print tweets['#ApjKalam'].value_counts()[True]
prg_langs = ['#AbdulKalam', '#kalam', '#ApjKalam']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['#kalam'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: #AbdulKalam vs. #kalam vs. #ApjKalam (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()