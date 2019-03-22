# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
import ssl
import bs4
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_189081.html'
html = urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, "html.parser")
# print(soup)
# Retrieve all of the anchor tags
comments = list()

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    comments.append(int(tag.contents[0]))
    # print('Attrs:', tag.attrs)
result = sum(comments)
print(result)
