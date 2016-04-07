#!/usr/bin/python

from random import randint

randInt = randint(1,16);
backgroundOptions = {1 : "aqua",
                     2 : "black",
                     3 : "blue",
                     4 : "fuchsia",
                     5 : "gray",
                     6 : "green",
                     7 : "lime",
                     8 : "maroon",
                     9 : "navy",
                     10 : "olive",
                     11 : "purple",
                     12 : "red",
                     13 : "silver",
                     14 : "teal",
                     15 : "white",
                     16 : "yellow",
                     }

backgroundColor = backgroundOptions[randInt]

varHeader = 'Content-type: text/html\n\n';
varHTMLStart= "<!doctype html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n"
varBody= "<body style=background-color:" +backgroundColor + ";" +">\n<h1>Hello World from Python @ YYYY</h1>\n</body>\n</html>";

print varHeader;
print varHTMLStart;
print varBody;
