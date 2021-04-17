import requests
import re
html = requests.get("https://www.wolframalpha.com/input/?i=HelloWorld").content
print(html.decode().split("</head>")[1])