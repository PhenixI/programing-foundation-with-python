# -*- coding: utf-8 -*-
import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and hist toys that come to life'",
                        "http://upload.wikimedia.org/wikipedia/en/l/13/Toy_Story.jpg",
                        "http://v.youku.com/v_show/id_XNTI2Njk5OTQ4.html?spm=a2hmv.20009921.yk-slide-94308.5~5!2~5~5!2~A&from=y1.3-movie-grid-1095-9921.94308.2-1"
                        )


#toy_story.show_trailer()
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post",
                     "plus")
#print(avatar.storyline)

movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)