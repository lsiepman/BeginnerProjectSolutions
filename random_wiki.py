# -*- coding: utf-8 -*-
r"""
Created on Sat Mar 14 21:48:01 2020.

Random Wikipedia Article

Create a program that pulls titles from the official Wikipedia API
and then asks the user one by one if he or she would like to read about
that article.
- Do something about unicode appearing in the title.
- Make the program pause once the user has selected an article to read,
and allow him or her to continue browsing different article
titles once finished reading.
- Allow the user to simply press ENTER to be asked about a new article.

@author: laura
"""

import requests
import webbrowser
import pyinputplus as pyip

class RandomWiki:
    """Offer a choice when using the random wiki api."""
    def __init__(self):
        self.url = None
        self.fetch_json()
        self.create_title_list()
        self.choose_article()

    def fetch_json(self):
        url = ("https://en.wikipedia.org/w/api.php?action=query&list=random&"
               + "rnnamespace=0&rnlimit=10&format=json")
        r = requests.get(url)
        if r.status_code != 200:
            print("Error fetching json")

        self.json = r.json()
        self.id_titles = self.json["query"]["random"]

    def create_title_list(self):
        self.titles = []
        self.ids = []
        for i in self.id_titles:
            self.titles.append(i["title"])
            self.ids.append(i["id"])

    def choose_article(self):
        if len(self.titles) == 0:
            self.again()
        else:
            message = f"Do you want to read about {self.titles[0]}? "
            answer = pyip.inputYesNo(message)

            if answer == "no":
                self.titles.pop(0)
                self.ids.pop(0)
                self.choose_article()
            else:
                self.open_page()



    def open_page(self):
        self.url = f"https://en.wikipedia.org/wiki?curid={self.ids[0]}"
        webbrowser.open(self.url)
        self.ids.pop(0)
        self.titles.pop(0)
        self.choose_article()

    def again(self):
        again = pyip.inputYesNo("Read more articles?")

        if again == "yes":
            self.fetch_json()
            self.create_title_list()
            self.choose_article()
        elif again == "no":
            print("See you later.")
        else:
            print("The computer is confused.")

rand = RandomWiki()

