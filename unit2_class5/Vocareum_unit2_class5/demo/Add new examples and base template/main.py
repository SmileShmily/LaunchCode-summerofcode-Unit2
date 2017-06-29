import os
  
  template_dir = os.path.join(os.path.dirname(__file__), 'templates')
 -jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
 +jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
 +    autoescape = True)
  
  class Handler(webapp2.RequestHandler):
  
 @@ -30,7 +31,7 @@ def get(self):
  class Hello(Handler):
  
      def get(self):
 -        self.render('hello.html', name=self.request.get('name'))
 +        self.render('hello.html', name=self.request.get('name', 'World'))
  
  
  class Caesar(Handler):
 @@ -122,11 +123,24 @@ def get(self):
          username = self.request.get("username")
          self.render('welcome.html', username=username)
  
 +class FizzBuzz(Handler):
 +
 +    def get(self):
 +        n = self.request.get('n', 0)
 +        self.render('fizzbuzz.html', title="FizzBuzz", n=int(n))
 +
 +class ShoppingList(Handler):
 +
 +    def get(self):
 +        items = self.request.get_all("food")
 +        self.render("shopping_list.html", title="Shopping List", items=items)
  
  app = webapp2.WSGIApplication([
      ('/', Index),
      ('/caesar', Caesar),
      ('/signup', Signup),
      ('/welcome', Welcome),
 -    ('/hello', Hello)
 +    ('/hello', Hello),
 +    ('/fizzbuzz', FizzBuzz),
 +    ('/shoppinglist', ShoppingList)
  ], debug=True)