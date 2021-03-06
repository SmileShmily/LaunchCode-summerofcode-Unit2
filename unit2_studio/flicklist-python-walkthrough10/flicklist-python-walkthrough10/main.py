import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db


# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# we'll use this template in a few places
t_scaffolding = jinja_env.get_template("scaffolding.html")

# a list of movies that nobody should be allowed to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives"
]


class Movie(db.Model):
    title = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    watched = db.BooleanProperty(required = True, default = False)
    rating = db.StringProperty()


def getUnwatchedMovies():
    """ Returns the list of movies the user wants to watch (but hasnt yet) """

    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]


def getWatchedMovies():
    """ Returns the list of movies the user has already watched """

    return [ "The Matrix", "The Big Green", "Ping Ping Playa" ]


class Handler(webapp2.RequestHandler):
    """ A base RequestHandler class for our app.
        The other handlers inherit form this one.
    """

    def renderError(self, error_code):
        """ Sends an HTTP error code and a generic "oops!" message to the client. """

        self.error(error_code)
        self.response.write("Oops! Something went wrong.")


class Index(Handler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):
        unwatched_movies = db.GqlQuery("SELECT * FROM Movie where watched = False")
        t_frontpage = jinja_env.get_template("frontpage.html")
        frontpage_content = t_frontpage.render(
                                movies = unwatched_movies,
                                error = self.request.get("error"))
        response = t_scaffolding.render(
                    title = "FlickList: Movies I Want to Watch",
                    content = frontpage_content)
        self.response.write(response)


class AddMovie(Handler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        new_movie_title = self.request.get("new-movie")

        # if the user typed nothing at all, redirect and yell at them
        if (not new_movie_title) or (new_movie_title.strip() == ""):
            error = "Please specify the movie you want to add."
            self.redirect("/?error=" + cgi.escape(error))

        # if the user wants to add a terrible movie, redirect and yell at them
        if new_movie_title in terrible_movies:
            error = "Trust me, you don't want to add '{0}' to your Watchlist.".format(new_movie_title)
            self.redirect("/?error=" + cgi.escape(error, quote=True))

        # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
        new_movie_title_escaped = cgi.escape(new_movie_title, quote=True)

        # construct a movie object for the new movie
        movie = Movie(title = new_movie_title_escaped)
        movie.put()

        # render the confirmation message
        t_add = jinja_env.get_template("add-confirmation.html")
        add_content = t_add.render(movie = new_movie_title_escaped)
        response = t_scaffolding.render(
                        title = "FlickList: Add a Movie",
                        content = add_content)
        self.response.write(response)


class WatchedMovie(Handler):
    """ Handles requests coming in to '/watched-it'
        e.g. www.flicklist.com/watched-it
    """

    def post(self):
        watched_movie_id = self.request.get("watched-movie")

        watched_movie = Movie.get_by_id( int(watched_movie_id) )

        # if we can't find the movie, reject.
        if not watched_movie:
            self.renderError(400)
            return

        # update the movie's ".watched" property to True
        watched_movie.watched = True
        watched_movie.put()

        # render confirmation page
        t_watched_it = jinja_env.get_template("watched-it-confirmation.html")
        watched_it_content = t_watched_it.render(movie = watched_movie)
        response = t_scaffolding.render(
                    title = "FlickList: Watched a Movie",
                    content = watched_it_content)
        self.response.write(response)


class MovieRatings(Handler):

    def get(self):
        # query for all the movies that have been watched, most recent first
        watched_movies = db.GqlQuery("SELECT * FROM Movie WHERE watched = True ORDER BY created desc")
        t_ratings = jinja_env.get_template("ratings.html")
        ratings_content = t_ratings.render(movies = watched_movies)
        response = t_scaffolding.render(
                    title = "FlickList: Movies I have Watched",
                    content = ratings_content)
        self.response.write(response)

    def post(self):
        movie_id = self.request.get("movie")
        movie = Movie.get_by_id( int(movie_id) )
        rating = self.request.get("rating")

        if movie and rating:
            # update movie.rating property
            movie.rating = rating
            movie.put()

            # render confirmation
            t_rating_confirmation = jinja_env.get_template("rating-confirmation.html")
            confirmation_content = t_rating_confirmation.render(movie = movie)
            response = t_scaffolding.render(
                        title = "FlickList: Movies I have Watched",
                        content = confirmation_content)
            self.response.write(response)
        else:
            self.renderError(400)
            return


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/watched-it', WatchedMovie),
    ('/ratings', MovieRatings)
], debug=True)
