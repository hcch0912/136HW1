#!/usr/bin/python

varHeader = 'Content-type: text/html\n\n';
varHTMLStart = '<!doctype html>\n<html>\n<head>\n<title>Python Form</title>\n</head>\n';
varBody = '<body>\n<h1>Form Test</h1>\n<hr>\n';

varFormGet = '<form action="responseData.py" method="GET">\n'
varFormPost = '<form action="responseData.py" method="GET">\n'
varUser = '<label>username: <input type="text" name="username"></label>\n<br>\n';
varPassword = '<label>userpassword: <input type="password" name="userpassword"></label>\n<br>\n';
varMagicNum = '<label>Magic Number: <input type="text" name="magicnum" size="2" maxlength="2"></label>\n<br>\n';
varInputs = '<input type="submit" value="send">\n</form>\n'

getContainer = varFormGet + varUser+  varPassword + varMagicNum + varInputs+"\n";
postContainer = varFormPost + varUser+  varPassword + varMagicNum + varInputs;
formContainer=getContainer+postContainer;

varCloseHTML = '</body>\n</html>\n'

print varHeader
print varHTMLStart
print varBody
print formContainer
print varCloseHTML
