# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:07:36 2019

@author: KMART11
"""

import tweepy

CONSUMER_KEY = 'oQQFMhxQ0K5lfL0lyXVxY4GEZ'
CONSUMER_SECRET = 'aLecmG5UIOlxLS6aOBqZAHQfmkb8T2LxRxUnNT811bLzleCDPM'
ACCESS_TOKEN = '1197303988972077058-Nhd7PD0b5BB2y2NQ1Z1Vxn1q6J2wch'
ACCESS_TOKEN_SECRET = 'fnFEBlfokHlbDKfnTvgQ9wbg9f0DRdvpVvTBSFKrWj1ws'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Python Class Rocks!"
api.update_status(status=status)