# -*- coding: utf-8 -*-

import webbrowser
class Movie():
    def __init__(self,movie_title,moive_storyline,poster_image,trainler_youtube):
        self.title=movie_title
        self.storyline= moive_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trainler_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    