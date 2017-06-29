#!/usr/bin/env python

import webapp2
from problem_sets import *
from examples import *
from tools import Handler

class Index(Handler):

    def get(self):
        self.render('index.html')


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/caesar', Caesar),
    ('/signup', Signup),
    ('/welcome', Welcome),
    ('/hello', Hello),
    ('/fizzbuzz', FizzBuzz),
    ('/shoppinglist', ShoppingList),
    ('/asciichan', AsciiChan)
], debug=True)
