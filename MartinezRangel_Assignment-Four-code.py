#!/usr/bin/env python
# coding: utf-8

# In[3]:


'hello tweepy'


# In[4]:


import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")


# In[11]:


import tweepy

consumer_key = "wXXXXXXXXXXXXXXXXXXXXXXX1"
consumer_secret = "qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi"
access_token_secret = "kXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXT"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object
api = tweepy.API(auth)


# In[1]:


import tweepy


BeautifulSoup: I know it's slow, but this library to parse xml and html code is very useful for those who are starting to program in Python.
s, attributes and values. To be more exact, the tree consists of four types of objects, Tag, NavigableString, BeautifulSoup and Comment. This tree can be "queried" using the methods / properties of the BeautifulSoup object that is created from the parser library.


# In[ ]:




