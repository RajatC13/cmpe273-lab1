import requests
r1 = requests.get('https://webhook.site/dbf057be-8834-464d-a48b-531a2be264a5')
print(r1.headers['Date'])

r2 = requests.get('https://webhook.site/dbf057be-8834-464d-a48b-531a2be264a5')
print(r2.headers['Date'])

r3 = requests.get('https://webhook.site/dbf057be-8834-464d-a48b-531a2be264a5')
print(r3.headers['Date'])
