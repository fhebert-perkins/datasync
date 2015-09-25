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
ROOT = "/home/finley" # make sure this is an absolute path
HOST = "localhost:8008"
USERNAME = "admin"
PASSWORD = "password"
# END VARIABLES

import requests
import os
import sys

print("Getting path list...")

r = requests.get("http://"+HOST+"/list", auth=(USERNAME, PASSWORD))

print("Done getting path list")

remote_paths = r.text.split("\n")
local_paths = []

for (dirpath, dirnames, filenames) in os.walk(ROOT):
    for filename in filenames:
        local_paths.append(os.path.join(dirpath.replace(ROOT,""), filename))

paths_to_dl = []

print("Compareing files in local and remote hosts")

for path in remote_paths:
    if path not in local_paths:
        paths_to_dl.append(path)

print(str(len(paths_to_dl))+" files to download")

sys.exit()

print("Creating file paths...")

for path in paths_to_dl:
    if not os.isdir("/".join(path.split("/")[:-1])):
        os.makedirs("/".join(path.split("/")[:-1]))

print("Getting files...")

for uri in paths_to_dl:
    os.system("curl -u "+USERNAME+":"+PASSWORD+" http://"+HOST+"/get/"+uri+" > "+ ROOT + uri)

print("Done")
