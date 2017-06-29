import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # list of movies to select from
        movies = ["The Big Lebowski", "Blue Velvet", "Toy Story", "Star Wars", "Amelie"]

        # randomly choose one of the movies
        randomIdx = random.randrange(len(movies))

        return movies[randomIdx]

    def get(self):
        # add Movie of the Day to the response string
        movie = self.getRandomMovie()
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        # add Tomorrow's Movie to the response string
        tomorrow_movie = self.getRandomMovie()
        response += "<h1>Tomorrow's Movie</h1>"
        response += "<p>" + tomorrow_movie + "</p>"

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)