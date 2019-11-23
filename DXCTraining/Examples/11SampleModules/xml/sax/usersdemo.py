#!/usr/bin/python
import xml.dom.minidom

# Open XML document using minidom parser
root = xml.dom.minidom.parse("users.xml")
users = root.documentElement
if users.hasAttribute("org"):
    print("Root element : %s" % users.getAttribute("org"))

for user in users.getElementsByTagName('user'):
    fname = user.getElementsByTagName('fname')[0]
    f = fname.childNodes[0].data
    lname = user.getElementsByTagName('lname')[0]
    l = lname.childNodes[0].data
    print(f, l)
