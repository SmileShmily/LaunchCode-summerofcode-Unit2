import webapp2
  from caesar import rotate_string
  import cgi
  import re
 +import jinja2
 +import os
 +
 +template_dir = os.path.join(os.path.dirname(__file__), 'templates')
 +jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
 +
 +class Handler(webapp2.RequestHandler):
 +
 +    def write(self, *a, **kw):
 +        self.response.out.write(*a, **kw)
 +
 +    def render_str(self, template, **params):
 +        t = jinja_env.get_template(template)
 +        return t.render(params)
  
 -class  MainHandler(webapp2.RequestHandler):
 +    def render(self, template, **kw):
 +        self.write(self.render_str(template, **kw))
  
 -    pages = [
 -        {'name': 'caesar', 'url': '/caesar'},
 -        {'name': 'signup', 'url': '/signup'}
 -    ]
 +class  index(Handler):
  
      def get(self):
 -        markup = "<h1>Web Fundamentals Demos</h1><ul>"
 -        item = "<li><a href='%(url)s'>%(name)s</a></li>"
 -
 -        for page in self.pages:
 -            markup = markup + (item % page)
 -
 -        markup = markup + "</ul>"
 -        self.response.out.write(markup)
 -
 -class CaesarHandler(webapp2.RequestHandler):
 -
 -    form = """
 -    <style>
 -        form {
 -            background-color: #eee;
 -            padding: 20px;
 -            margin: 0 auto;
 -            width: 540px;
 -            font: 16px sans-serif;
 -            border-radius: 10px;
 -        }
 -        textarea {
 -            margin: 10px 0;
 -        }
 -    </style>
 -    <form method="post">
 -        <div>
 -            <label for="rot">Rotate by:</label>
 -            <input type="text" name="rot" required size=2>
 -            <p style="color:red">%(error)s</p>
 -        </div>
 -        <textarea type="text" name="text" rows=20 cols=80>%(text)s</textarea>
 -        <br>
 -        <input type="submit">
 -    </form>
 -    """
 -
 -    def write_form(self, text="", error=""):
 -        self.response.out.write(self.form % {"text": text, "error": error})
 +
 +        pages = [
 +            {'name': 'caesar', 'url': '/caesar'},
 +            {'name': 'signup', 'url': '/signup'}
 +        ]
 +
 +        self.render('index.html', pages=pages)
 +
 +class caesar(Handler):
  
      def get(self):
 -        self.write_form()
 +        self.render('caesar.html')
  
      def post(self):
  
 @@ -79,62 +47,11 @@ def post(self):
          if rot.isdigit():
              rot = int(rot)
              text = rotate_string(text, rot)
 -            self.write_form(cgi.escape(text))
 +            self.render('caesar.html', text=cgi.escape(text))
          else:
 -            self.write_form(cgi.escape(text), "Please enter a valid number")
 -
 -class SignupHandler(webapp2.RequestHandler):
 -
 -    form = """
 -    <style>
 -        .error {
 -            color: red;
 -        }
 -    </style>
 -    <h1>Signup</h1>
 -    <form method="post">
 -        <table>
 -            <tr>
 -                <td><label for="username">Username</label></td>
 -                <td>
 -                    <input name="username" type="text" value="%(username)s" required>
 -                    <span class="error">%(username_error)s</span>
 -                </td>
 -            </tr>
 -            <tr>
 -                <td><label for="password">Password</label></td>
 -                <td>
 -                    <input name="password" type="password" required>
 -                    <span class="error">%(password_error)s</span>
 -                </td>
 -            </tr>
 -            <tr>
 -                <td><label for="verify">Verify Password</label></td>
 -                <td>
 -                    <input name="verify" type="password" required>
 -                    <span class="error">%(verify_error)s</span>
 -                </td>
 -            </tr>
 -            <tr>
 -                <td><label for="email">Email (optional)</label></td>
 -                <td>
 -                    <input name="email" type="email" value="%(email)s">
 -                    <span class="error">%(email_error)s</span>
 -                </td>
 -            </tr>
 -        </table>
 -        <input type="submit">
 -    </form>
 -    """
 -
 -    def write_form(self, username="", email="", username_error="", password_error="", verify_error="", email_error=""):
 -        values = { 'username': username,
 -            'email': email,
 -            'username_error': username_error,
 -            'password_error': password_error,
 -            'verify_error':  verify_error,
 -            'email_error': email_error}
 -        self.response.out.write(self.form % values)
 +            self.render('caesar.html', text=cgi.escape(text), error="Please enter a valid number")
 +
 +class signup(Handler):
  
      def validate_username(self, username):
          USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
 @@ -165,7 +82,7 @@ def validate_email(self, email):
              return email
  
      def get(self):
 -        self.write_form()
 +        self.render('signup.html')
  
      def post(self):
  
 @@ -183,36 +100,32 @@ def post(self):
              self.redirect('/welcome?username=%s' % username)
          else:
  
 -            username_error = ""
 -            password_error = ""
 -            verify_error = ""
 -            email_error = ""
 +            errors = {}
  
              if not username:
 -                username_error = "That's not a valid username"
 +                errors['username_error'] = "That's not a valid username"
  
              if not password:
 -                password_error = "That's not a valid password"
 +                errors['password_error'] = "That's not a valid password"
  
              if not verify:
 -                verify_error = "Passwords don't match"
 +                errors['verify_error'] = "Passwords don't match"
  
              if email is None:
 -                email_error = "That's not a valid email"
 -
 -            self.write_form(username, email, username_error, password_error, verify_error, email_error)
 +                errors['email_error'] = "That's not a valid email"
  
 +            self.render('signup.html', username=username, email=email, errors=errors)
  
 -class WelcomeHandler(webapp2.RequestHandler):
 +class welcome(Handler):
  
      def get(self):
          username = self.request.get("username")
 -        self.response.out.write("<h1>Welcome, %s!</h1>" % username)
 +        self.render('welcome.html', username=username)
  
  
  app = webapp2.WSGIApplication([
 -    ('/', MainHandler),
 -    ('/caesar', CaesarHandler),
 -    ('/signup', SignupHandler),
 -    ('/welcome', WelcomeHandler)
 +    ('/', index),
 +    ('/caesar', caesar),
 +    ('/signup', signup),
 +    ('/welcome', welcome)
  ], debug=True)