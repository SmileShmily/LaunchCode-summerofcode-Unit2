#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2, cgi

form="""
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(answer)s</textarea>
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
        rotate = int(self.request.get('rot'))
        output = cgi.escape(self.caesar(content, rotate), quote = True)
        self.response.write(form % {'answer': output    })

    def caesar(self,string, rot):
        ret = ''
        for i in string:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                ret += chr((ord(i)-ord('a')+rot)%26+ord('a'))
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                ret += chr((ord(i)-ord('A')+rot)%26+ord('A'))
            else:
                ret += i
        return ret


app = webapp2.WSGIApplication([('/', MainPage)],debug=True)
