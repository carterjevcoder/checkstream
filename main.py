#!/usr/bin/env python3
# AUTHOR: Carter Jevens
# PROGRAM: checkstream
# PURPOSE: Scrapes justwatch to see what services are available to stream and buy media.

#imports needed to scrape HTML
from bs4 import BeautifulSoup
import requests
import string


user_input = input("Are you trying to watch a TV show or movie? (t/m): ")

while user_input != "t" and user_input != "m":
    user_input = input("Error, enter with the correct format. 't/m': ")
    if user_input == "t" or user_input == "m":
        break


title_media = input("WHAT U WANNA WATCH? ")
for char in string.punctuation:
    title_media = title_media.replace(char, '')
title_media = title_media.replace(" ", "-")

print (title_media)

if user_input == "t":
    url = "https://www.justwatch.com/us/tv-show/" + title_media

if user_input == "m":
    url = "https://www.justwatch.com/us/movie/" + title_media

print(url)



