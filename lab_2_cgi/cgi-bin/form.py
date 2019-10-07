#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
mail = html.escape(form.getfirst("mail", "не задано"))
radio = html.escape(form.getfirst("radio", "не задано"))
check = html.escape(form.getfirst("check", "не задано"))
password = html.escape(form.getfirst("password", "не задано"))

print("Content-type: text/html\n")
print(
    """<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Обробка даних форми</title>
</head>
<body>
"""
)

print("<h1>Оброблені дані форми!</h1>")
print(f"<p>mail: {mail}</p>")
print(f"<p>password: {password}</p>")
print(f"<p>radio: {radio}</p>")
print(f"<p>checked: {check}</p>")

print(
    """</body>
</html>
"""
)
