import webapp2
 +from caesar import rotate_string
 +import cgi
 +
 +class  MainHandler(webapp2.RequestHandler):
 +
 +    pages = [
 +        {'name': 'caesar', 'url': '/caesar'},
 +        {'name': 'signup', 'url': '/signup'}
 +    ]
 +
 +    def get(self):
 +        markup = "<h1>Web Fundamentals Demos</h1><ul>"
 +        item = "<li><a href='%(url)s'>%(name)s</a></li>"
 +
 +        for page in self.pages:
 +            markup = markup + (item % page)
 +
 +        markup = markup + "</ul>"
 +        self.response.out.write(markup)
 +
 +class CaesarHandler(webapp2.RequestHandler):
 +
 +    form = """
 +    <style>
 +        form {
 +            background-color: #eee;
 +            padding: 20px;
 +            margin: 0 auto;
 +            width: 540px;
 +            font: 16px sans-serif;
 +            border-radius: 10px;
 +        }
 +        textarea {
 +            margin: 10px 0;
 +        }
 +    </style>
 +    <form method="post">
 +        <div>
 +            <label for="rot">Rotate by:</label>
 +            <input type="text" name="rot" required size=2>
 +            <p style="color:red">%(error)s</p>
 +        </div>
 +        <textarea type="text" name="text" rows=20 cols=80>%(text)s</textarea>
 +        <br>
 +        <input type="submit">
 +    </form>
 +    """
 +
 +    def write_form(self, text="", error=""):
 +        self.response.out.write(self.form % {"text": text, "error": error})
 +
 +    def get(self):
 +        self.write_form()
 +
 +    def post(self):
 +
 +        rot = self.request.get("rot")
 +        text = self.request.get("text")
 +
 +        #validate input
 +        if rot.isdigit():
 +            rot = int(rot)
 +            text = rotate_string(text, rot)
 +            self.write_form(cgi.escape(text))
 +        else:
 +            self.write_form(cgi.escape(text), "Please enter a valid number")
 +
 +class SignupHandler(webapp2.RequestHandler):
 +
 +    def write_form():
 +        pass
 +
 +    def get(self):
 +        self.response.out.write('hey!')
 +
 +
 +app = webapp2.WSGIApplication([
 +    ('/', MainHandler),
 +    ('/caesar', CaesarHandler),
 +    ('/signup', SignupHandler)
 +], debug=True)