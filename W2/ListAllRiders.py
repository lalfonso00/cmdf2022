import http.client
import urllib.parse
import json

conn = http.client.HTTPSConnection("api.sparelabs.com")

headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}
params = {'email': "adam.kobayashi.hrvswa1rng@bot.sparelabs.com"}
conn.request("GET", "/v1/riders?" +
             urllib.parse.urlencode(params), headers=headers)
# conn.request("GET", "/v1/riders", headers=headers)

res = conn.getresponse()
data = res.read()


rider = data.decode("utf-8")

r = json.loads(rider)

print(r["data"][0]["id"])
