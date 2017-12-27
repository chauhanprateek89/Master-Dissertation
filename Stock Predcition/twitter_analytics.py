# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 02:39:47 2017

@author: Prateek Chauhan
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "745154744-tSnfUVUszUVUhnt9zGVMXwz6oSJgKeiQZYONyUJ4"
access_token_secret = "hWuPMLegeriF6fououxojQBdo7hNOoaiQnCfrhVE6Z3MH"
consumer_key = "nhyXflsoKR06gKNHF2yMu0RIf"
consumer_secret = "hDZB184na2ufOgrnTsETgL3GpXxGEEQqt8T3TnIdeMPmdxHWhI"

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self,status):
        print(status)
        
if __name__ == '__main__':
    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth, l)
    
    stream.filter(track=['RCOM','RELCAPITAL',"RELIANCE JIO", "Reliance Industries" ,'RELINFRA','RPOWER' , 'RELBANK' , 'RDEL','RELGOLD' ,'RELMEDIA'])