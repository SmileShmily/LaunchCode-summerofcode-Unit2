#!/usr/bin/env python
#

import webapp2, cgi

form="""
<html>
  <head>
    <title> Caesar</title>
  </head>

  <body>
    <h2>Enter some text to caesar:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(answer)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form % {'answer': ''})

    def post(self):
        content = self.request.get('text')
        output = cgi.escape(self.caesar(content), quote = True)
        self.response.write(form % {'answer': output    })

    def caesar(self,string):
        ret = ''
        for i in string:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                ret += chr((ord(i)-ord('a')+13)%26+ord('a'))
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                ret += chr((ord(i)-ord('A')+13)%26+ord('A'))
            else:
                ret += i
        return ret

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
