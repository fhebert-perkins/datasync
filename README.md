# Data Sync
Copy files between a client and a servers file system over HTTP.

## Installation

### Server

```
git clone http://github.com/fhebert-perkins/datasync
cd datasync
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python server/main.py
```

Server will now run on port 8008 by default. Default username is "admin" and password is "password"

There are two paths as the API, ```/list``` and ```/get```

```/list``` gets all files in the root directory as defined by ROOT in main.py
/get downloads the file at ```/get/$path```

Both paths are protected by HTTP simple auth whose username and password can be changed by changing the ```USERNAME``` and ```PASSWORD``` variables in main.py

### Client
```
git clone http://github.com/fhebert-perkins/datasync
cd datasync
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python client/main.py
```

This will query all folder in the index files on the server and then sync those files with itself over HTTP.

## Misc

These scripts were built for the [tuolumne skies observatory](http://www.tuolumneskies.com/observatory/) in order to copy photos automatically to The Bay School of San Francisco Astronomy Lab.
