#!/usr/bin/python

import os

varHeader = 'Content-type: text/html\n\n';
varHTMLStart= "<!doctype html>\n<html>\n<head>\n<title>Hello Env Python</title>\n</head>\n"

envList = "";
sortedOsEnv = sorted(os.environ.keys())
for key in sortedOsEnv:
    envList +="<li>" + key + ": " + os.environ[key] +"</li>\n"

listwrapper = "<h1>Server Env</h1>\n<ul>\n" +envList +"</ul>\n"

content = listwrapper

varBody= "<body>\n"+content+"</body>\n</html>"

print os.environ["BROWSER"]

print varHeader
print varHTMLStart
print varBody
