 rot = self.request.get("rot")
          text = self.request.get("text")
  
 -        #validate input
 -        if rot.isdigit():
 -            rot = int(rot)
 -            text = rotate_string(text, rot)
 -            self.render('caesar.html', text=cgi.escape(text))
 -        else:
 -            self.render('caesar.html', text=cgi.escape(text), error="Please enter a valid number")
 +        rot = int(rot)
 +        text = rotate_string(text, rot)
 +        self.render('caesar.html', text=cgi.escape(text))
  class Signup(Handler):