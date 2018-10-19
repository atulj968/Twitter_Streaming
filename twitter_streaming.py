#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:51:46 2018

@author: atuljain
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

acces_token ="##################################"        #Enter your Acces- token key  
access_token_secret="#################################"  #Enter your access-token-secret key
consumer_key="#########################"                #Enter your consumer key
consumer_secret ="###############################################" #Enter your secret consumer key
class StdoutListener(StreamListener):
    def on_data(self,data):
            print data
            return True
        
    def ob_error(self,status):
        print status
        
if __name__ =="__main__":
    l =StdoutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acces_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track = ['#AbdulKalam','#kalam','#ApjKalam','#KejriwalCalls4Donation13K Tweets','#RahulGandhiInGwalior'])
    time.sleep(6/60)
