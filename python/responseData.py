#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
magicnum  = form.getvalue('magicnum')
userpassword = form.getvalue('userpassword')

outputMsg = ""
for i in range(0, magicnum):
    outputMsg+="<h1>Hello " + username + " with a password of " + userpassword+"!</h1>\n"

varHeader = 'Content-type: text/html\n\n';
varHTMLStart= "<!doctype html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n"
varBody= "<body>\n"+outputMsg+"</body>\n</html>";

print varHeader+varHTMLStart+varBody
