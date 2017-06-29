import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, Summer of Code!')

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
