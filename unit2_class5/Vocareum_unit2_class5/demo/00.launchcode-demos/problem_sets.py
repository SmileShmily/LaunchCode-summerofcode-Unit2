import cgi, re
from caesar import rotate_string
from tools import Handler

class Caesar(Handler):

    def get(self):
        self.render('caesar.html')

    def post(self):

        rot = self.request.get("rot")
        text = self.request.get("text")

        rot = int(rot)
        text = rotate_string(text, rot)
        self.render('caesar.html', text=cgi.escape(text))


class Signup(Handler):

    def validate_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if USER_RE.match(username):
            return username
        else:
            return ""

    def validate_password(self, password):
        PWD_RE = re.compile(r"^.{3,20}$")
        if PWD_RE.match(password):
            return password
        else:
            return ""

    def validate_verify(self, password, verify):
        if password == verify:
            return verify

    def validate_email(self, email):

        # allow empty email field
        if not email:
            return ""

        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        if EMAIL_RE.match(email):
            return email

    def get(self):
        self.render('signup.html', errors={})

    def post(self):

        submitted_username = self.request.get("username")
        submitted_password = self.request.get("password")
        submitted_verify = self.request.get("verify")
        submitted_email = self.request.get("email")

        username = self.validate_username(submitted_username)
        password = self.validate_password(submitted_password)
        verify = self.validate_verify(submitted_password, submitted_verify)
        email = self.validate_email(submitted_email)

        if (username and password and verify and (email is not None) ):
            self.redirect('/welcome?username=%s' % username)
        else:

            errors = {}

            if not username:
                errors['username_error'] = "That's not a valid username"

            if not password:
                errors['password_error'] = "That's not a valid password"

            if not verify:
                errors['verify_error'] = "Passwords don't match"

            if email is None:
                errors['email_error'] = "That's not a valid email"

            self.render('signup.html', username=username, email=email, errors=errors)

class Welcome(Handler):

    def get(self):
        username = self.request.get("username")
        self.render('welcome.html', username=username)
