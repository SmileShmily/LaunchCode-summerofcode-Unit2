def render(self, template, **kw):
          self.write(self.render_str(template, **kw))
  
 -class  index(Handler):
 +class Index(Handler):
  
      def get(self):
 +        self.render('index.html')
  
 -        pages = [
 -            {'name': 'caesar', 'url': '/caesar'},
 -            {'name': 'signup', 'url': '/signup'}
 -        ]
 +class Hello(Handler):
 +
 +    def get(self):
 +        self.render('hello.html', name=self.request.get('name'))
  
 -        self.render('index.html', pages=pages)
  
 -class caesar(Handler):
 +class Caesar(Handler):
  
      def get(self):
          self.render('caesar.html')
 @@ -51,7 +51,7 @@ def post(self):
          else:
              self.render('caesar.html', text=cgi.escape(text), error="Please enter a valid number")
  
 -class signup(Handler):
 +class Signup(Handler):
  
      def validate_username(self, username):
          USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
 @@ -116,16 +116,17 @@ def post(self):
  
              self.render('signup.html', username=username, email=email, errors=errors)
  
 -class welcome(Handler):
 +class Welcome(Handler):
  
      def get(self):
          username = self.request.get("username")
          self.render('welcome.html', username=username)
  
  
  app = webapp2.WSGIApplication([
 -    ('/', index),
 -    ('/caesar', caesar),
 -    ('/signup', signup),
 -    ('/welcome', welcome)
 +    ('/', Index),
 +    ('/caesar', Caesar),
 +    ('/signup', Signup),
 +    ('/welcome', Welcome),
 +    ('/hello', Hello)
  ], debug=True)