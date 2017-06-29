from tools import Handler
from google.appengine.ext import db

class Hello(Handler):

    def get(self):
        self.render('hello.html', name=self.request.get('name', 'World'))

class FizzBuzz(Handler):

    def get(self):
        n = self.request.get('n', 0)
        self.render('fizzbuzz.html', title="FizzBuzz", n=int(n))

class ShoppingList(Handler):

    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", title="Shopping List", items=items)

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class AsciiChan(Handler):

    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("asciichan.html", title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_front()

    @db.transactional
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title=title, art=art)
            a.put()
            self.redirect("/asciichan")
        else:
            error = "we need both a title and art!"
            self.render_front(title, art, error)
