# The MIT License (MIT)
#
# Copyright (c) 2015 Finley Hebert-Perkins
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# VARIABLES
ROOT = "/home/finley"
PORT = 8008
HOST = "localhost"
USERNAME = "admin"
PASSWORD = "password"
# END OF VARIABLES

from bottle import route, run, auth_basic, static_file
import os

def check(user, pw):
    if user == USERNAME and pw == PASSWORD:
        return True
    else:
        return False

@route("/list")
@auth_basic(check)
def list():
    outstring = ""
    for (dirpath, dirnames, filenames) in os.walk(ROOT):
        for filename in filenames:
            outstring+= os.path.join(dirpath.replace(ROOT,""), filename) + "\n"
    return outstring
@route("/get/<path:path>")
@auth_basic(check)
def get(path):
    if os.path.exists(os.path.join(ROOT, path)):
        return static_file(path, root=ROOT, download=path)
    else:
        abort(404)

run(host=HOST, port=PORT)
