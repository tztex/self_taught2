import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = list()
URL = 'http://py4e-data.dr-chuck.net/comments_189084.json'
uh = urllib.request.urlopen(URL, context=ctx)
data = uh.read().decode()
js = json.loads(data)  # parse data from google and get dict object back
# print(json.dumps(js, indent=4))
# print(len(js))

for item in js["comments"]:
    counts.append(item["count"])
results = sum(counts)
print(results)