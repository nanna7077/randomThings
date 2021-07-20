#!/usr/bin/python

""" Download's n number of cat pictures to the current directory or specified directory

Usage:
python getcats.py n		    n    -> number of pictures	      -> INT
python getcats.py n path	    path -> path to save cat pics to  -> STRING
python getcats.py n path apikey     apikey -> CatAPI's API Key        -> STRING
"""

import requests
import sys
import socket

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False

if not is_connected():
    print("[ERROR] Internet not available. T-T")
    exit(1)

try:
    n = int(sys.argv[1])
except:
    n = 1
try:
    path = sys.argv[2].rstrip("/")
    path += "/"
except:
    path = ""
try:
    apikey = sys.argv[3]
except:
    apikey = ""

count=1
while count<=n:
    print("[LOG] Fetching {}/{} mewmew's".format(count, n))
    req = requests.get("https://api.thecatapi.com/v1/images/search?api_key={}".format(apikey))
    if req:
        tdict = eval(req.content)[0]
        filename=tdict['url'].split("/")[-1].strip()
        req2 = requests.get(tdict['url'], stream = True)
        if req2:
            try:
                with open(path+filename, 'wb') as f:
                    f.write(req2.content)
            except:
                print("[ERROR] Path does not exist.")
                exit(1)
        print("[LOG] Saved {}".format(filename))
    count+=1

print("[BYE] Finished getting kitties.")
