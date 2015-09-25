import requests
import os
import sys

print("Getting path list...")

r = requests.get("http://localhost:8008/list", auth=("admin", "password"))

print("Done getting path list")

remote_paths = r.text.split("\n")
local_paths = []

for (dirpath, dirnames, filenames) in os.walk("/home/finley"):
    for filename in filenames:
        local_paths.append(os.path.join(dirpath.replace("/home/finley",""), filename))

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
    os.system("curl -u admin:password http://localhost:8008/get/"+uri+" > "+uri)

print("Done")
