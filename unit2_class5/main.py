#!/usr/bin/env python
#

import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")  
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

form="""
<form method="post" action="/ps2-1" >

	<textarea name="text" >%(message)s</textarea>
	<br />

	<div style="color: red;">%(error)s</div>
	<input type="submit" >

</form>
"""

form_signup="""
<form method="post" action="/ps2-2" >

	<div> Username: <input type = "text" name = "username" value = "%(username)s" /> <span style="color: red;"> %(username_error)s </span></div>
	<br />
	<div> Password: <input type = "text" name = "password" /> <span style="color: red;"> %(password_error)s </span></div>
	<br />
	<div> Verify password: <input type = "text" name = "verify" /> <span style="color: red;"> %(verify_error)s </span></div>
	<br />
	<div> Email: <input type = "text" name = "email" value = "%(email)s" /> <span style="color: red;"> %(email_error)s </span></div>
	<br />
	
	<input type="submit" >

</form>
"""

class PS21Handler(webapp2.RequestHandler):

	# Replaces some raw HTML chars to escape chars
	#
	def escape_html(self, s):
		repl_dict = {'>' : '&gt;', '<': '&lt;', '"': '&quot;', '&': '&amp;'}
		for i, j in repl_dict.iteritems():
			s = s.replace(i, j)
		return s

	# Encodes/decodes given string by ROT13 cipher (Caesar cipher)
	# 13/06/13 Deployed at http://kostylevv.appspot.com/ps2-1
	def rot13(self, string_to_replace):
		#replacement dictionary
		repl_dict = {'a' : 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
					 'g' : 't', 'h': 'u', 'i': 'v', 'k': 'x', 'l': 'y', 'm': 'z', 'j' : 'w',
					 'n' : 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f',
					 't' : 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
					 'A' : 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
					 'G' : 'T', 'H': 'U', 'I': 'V', 'K': 'X', 'L': 'Y', 'M': 'Z', 'J' : 'W',
					 'N' : 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
					 'T' : 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
		list_string = list(string_to_replace) #convert unicode word to list, 
											  #to be able to access by index
		#walking our word, char by char 
		for i in range(0, len(list_string)):
			if (repl_dict.has_key(list_string[i])):  #if we have replacement for current char
				list_string[i] = repl_dict[list_string[i]] #then - replace		
		
		string_to_replace = ''.join(list_string) #finally joining our list back to string
		return string_to_replace

	def write_form(self, message, error=""):
		self.response.out.write(form % {"error": error, "message": message})

	def get(self):
		self.write_form('','')

	def post(self):
		text = self.request.get("text")
		message = self.rot13(text)
		message = self.escape_html(message)
		self.write_form(message, text)


class PS22Handler(webapp2.RequestHandler):
	def valid_username(self, username):
		return USER_RE.match(username)

	def valid_password(self, password):
		return PASS_RE.match(password)

	def valid_email(self, email):
		if email == '':
			return True
		else:
			return EMAIL_RE.match(email)
		

	def write_form(self, username, email, username_error, 
				   password_error, verify_error, email_error):

		self.response.out.write(form_signup % {"username_error": username_error, 
											   "password_error": password_error, 
											   "email_error": email_error,
											   "username": username, 
											   "email": email,
											   "verify_error": verify_error})

	def get(self):
		self.write_form('','','','','','')

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")

		username_error = ''
		password_error = ''
		verify_error = ''
		email_error = ''
		valid = True
		
		if not self.valid_username(username):
			username_error = "Username is invalid"
			valid = False

		if password != verify:
			verify_error = 'Not matching passwords'
			valid = False
		else:
			if not self.valid_password(password):
				password_error = "Password is invalid"
				valid = False

		if email != '' and not self.valid_email(email):
			email_error = "Email is invalid"
			valid = False

		if not valid:
			self.write_form(username, email, username_error, password_error, 
							verify_error, email_error)
		else:
			self.redirect("/welcome?username="+self.request.get("username"))



class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Welcome, ' + self.request.get("username") + '!')


app = webapp2.WSGIApplication([('/ps2-1', PS21Handler),
							   ('/ps2-2', PS22Handler),
							   ('/welcome', WelcomeHandler)], 
							   debug=True)
