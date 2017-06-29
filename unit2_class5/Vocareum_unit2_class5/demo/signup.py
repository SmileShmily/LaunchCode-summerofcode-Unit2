import webapp2
  from caesar import rotate_string
  import cgi
 +import re
  
  class  MainHandler(webapp2.RequestHandler):
  
 @@ -84,15 +85,134 @@ def post(self):
  
  class SignupHandler(webapp2.RequestHandler):
  
 -    def write_form():
 -        pass
 +    form = """
 +    <style>
 +        .error {
 +            color: red;
 +        }
 +    </style>
 +    <h1>Signup</h1>
 +    <form method="post">
 +        <table>
 +            <tr>
 +                <td><label for="username">Username</label></td>
 +                <td>
 +                    <input name="username" type="text" value="%(username)s" required>
 +                    <span class="error">%(username_error)s</span>
 +                </td>
 +            </tr>
 +            <tr>
 +                <td><label for="password">Password</label></td>
 +                <td>
 +                    <input name="password" type="password" required>
 +                    <span class="error">%(password_error)s</span>
 +                </td>
 +            </tr>
 +            <tr>
 +                <td><label for="verify">Verify Password</label></td>
 +                <td>
 +                    <input name="verify" type="password" required>
 +                    <span class="error">%(verify_error)s</span>
 +                </td>
 +            </tr>
 +            <tr>
 +                <td><label for="email">Email (optional)</label></td>
 +                <td>
 +                    <input name="email" type="email" value="%(email)s">
 +                    <span class="error">%(email_error)s</span>
 +                </td>
 +            </tr>
 +        </table>
 +        <input type="submit">
 +    </form>
 +    """
 +
 +    def write_form(self, username="", email="", username_error="", password_error="", verify_error="", email_error=""):
 +        values = { 'username': username,
 +            'email': email,
 +            'username_error': username_error,
 +            'password_error': password_error,
 +            'verify_error':  verify_error,
 +            'email_error': email_error}
 +        self.response.out.write(self.form % values)
 +
 +    def validate_username(self, username):
 +        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
 +        if USER_RE.match(username):
 +            return username
 +        else:
 +            return ""
 +
 +    def validate_password(self, password):
 +        PWD_RE = re.compile(r"^.{3,20}$")
 +        if PWD_RE.match(password):
 +            return password
 +        else:
 +            return ""
 +
 +    def validate_verify(self, password, verify):
 +        if password == verify:
 +            return verify
 +
 +    def validate_email(self, email):
 +
 +        # allow empty email field
 +        if not email:
 +            return ""
 +
 +        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
 +        if EMAIL_RE.match(email):
 +            return email
 +
 +    def get(self):
 +        self.write_form()
 +
 +    def post(self):
 +
 +        submitted_username = self.request.get("username")
 +        submitted_password = self.request.get("password")
 +        submitted_verify = self.request.get("verify")
 +        submitted_email = self.request.get("email")
 +
 +        username = self.validate_username(submitted_username)
 +        password = self.validate_password(submitted_password)
 +        verify = self.validate_verify(submitted_password, submitted_verify)
 +        email = self.validate_email(submitted_email)
 +
 +        if (username and password and verify and (email is not None) ):
 +            self.redirect('/welcome?username=%s' % username)
 +        else:
 +
 +            username_error = ""
 +            password_error = ""
 +            verify_error = ""
 +            email_error = ""
 +
 +            if not username:
 +                username_error = "That's not a valid username"
 +
 +            if not password:
 +                password_error = "That's not a valid password"
 +
 +            if not verify:
 +                verify_error = "Passwords don't match"
 +
 +            if email is None:
 +                email_error = "That's not a valid email"
 +
 +            self.write_form(username, email, username_error, password_error, verify_error, email_error)
 +
 +
 +class WelcomeHandler(webapp2.RequestHandler):
  
      def get(self):
 -        self.response.out.write('hey!')
 +        username = self.request.get("username")
 +        self.response.out.write("<h1>Welcome, %s!</h1>" % username)
  
  
  app = webapp2.WSGIApplication([
      ('/', MainHandler),
      ('/caesar', CaesarHandler),
 -    ('/signup', SignupHandler)
 +    ('/signup', SignupHandler),
 +    ('/welcome', WelcomeHandler)
  ], debug=True)