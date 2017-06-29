<form method="post">
              <div>
                  <label for="rot">Rotate by:</label>
 -                <input type="number" step="1" name="rot" required size=2>
 +                <input type="text" name="rot" value="0">
                  <p class="error">{{ error }}</p>
              </div>
              <textarea type="text" name="text">{{ text }}</textarea>

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
 +
  
  class Signup(Handler):




	  <form method="post">
              <div>
                  <label for="rot">Rotate by:</label>
 -                <input type="text" name="rot" required size=2>
 +                <input type="number" step="1" name="rot" required size=2>
                  <p class="error">{{ error }}</p>
              </div>
              <textarea type="text" name="text">{{ text }}</textarea>