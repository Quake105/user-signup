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
import webapp2
import cgi
import re



class MainHandler(webapp2.RequestHandler):
    def get(self):

        form="""
        <html><head>
                <style>
                    .error {
                        color: red;
                    }
                </style>
            </head>
            <body>
            <h1>Signup</h1>
                <form method="post">
                    <table>
                        <tbody><tr>
                            <td><label for="username">Username</label></td>
                            <td>
                                <input name="username" type="text" value="" required="">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="password">Password</label></td>
                            <td>
                                <input name="password" type="password" required="">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="verify">Verify Password</label></td>
                            <td>
                                <input name="verify" type="password" required="">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="email">Email (optional)</label></td>
                            <td>
                                <input name="email" type="email" value="">
                                <span class="error"></span>
                            </td>
                        </tr>
                    </tbody></table>
                    <input type="submit">
                </form>

        </body></html>
        """

        self.response.out.write(form)

    def post(self, emailerror="", usererror="", passworderror="", username="", email=""):

        form="""
        <html><head>
                <style>
                    .error {
                        color: red;
                    }
                </style>
            </head>
            <body>
            <h1>Signup</h1>
                <form method="post">
                    <table>
                        <tbody><tr>
                            <td><label for="username">Username</label></td>
                            <td>
                                <input name="username" type="text" value="%(username)s" required="">
                                <span class="error">%(usererror)s</span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="password">Password</label></td>
                            <td>
                                <input name="password" type="password" required="">
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="verify">Verify Password</label></td>
                            <td>
                                <input name="verify" type="password" required="">
                                <span class="error">%(passworderror)s</span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="email">Email (optional)</label></td>
                            <td>
                                <input name="email" type="email" value="%(email)s">
                                <span class="error">%(emailerror)s</span>
                            </td>
                        </tr>
                    </tbody></table>
                    <input type="submit">
                </form>

        </body></html>
        """
        password = self.request.get('password')
        password = escape_htmls(password)


        verify = self.request.get('verify')
        verify = escape_htmls(verify)
        #def valid_password(password,verify):

        if password == verify:
            passworderror = ""
        else:
            passworderror = "Passwords do not match!"


        email = str(self.request.get('email'))
        email = escape_htmls(email)
        if re.compile("^[\w.-]+@[\w.-]+\.\w+$").match(email):
            emailerror = ""
        else:
            emailerror = "Email is not valid, please check"

        username = str(self.request.get('username'))
        username = escape_htmls(username)
        if re.compile("^\w+\s\w+$").match(username):
            usererror = "Username is not valid, please do not use space!"

        self.response.out.write(form % {"email": email, "username": username, "usererror": usererror, "passworderror": passworderror,
                                         "emailerror": emailerror
                                         })

def escape_htmls(s):
    return cgi.escape(s, quote=True)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
