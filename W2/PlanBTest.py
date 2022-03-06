# import http.client

# conn = http.client.HTTPSConnection("api.sparelabs.com")

# payload = "{\n  \"url\": \"string\",\n  \"types\": [\n    \"requestStatus\"\n  ],\n  \"headers\": [\n    {\n      \"key\": \"string\",\n      \"value\": \"string\"\n    }\n  ]\n}"

# headers = { 'Content-Type': "application/json", 'Authorization':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw" }

# conn.request("POST", "/v1/webhooks", payload, headers)

# res = conn.getresponse()
# data = res.read()




import http.client
conn = http.client.HTTPSConnection("api.sparelabs.com")

def createRider():
    # fname = input()
    # lname = input()
    # phoneNum = input()
    # email = input()

    # payload = {'firstName':fname , 'lastName': lname, 'photoUrl': null, 'email': email, 'metadata': {}, 'defaultRiders': }
    payload = "{\n  \"firstName\": \"Lo\",\n  \"lastName\": \"Al\",\n  \"photoUrl\": null,\n  \"phoneNumber\": \"6045559555\",\n  \"email\": \"ljl@gmail.com\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": 3\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    # payload = "{\n  \"firstName\": \"string\",\n  \"lastName\": \"string\",\n  \"photoUrl\": \"string\",\n  \"phoneNumber\": \"string\",\n  \"email\": \"string\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    headers = { 'Content-Type': "application/json", 'Authorization':"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw" }

    conn.request("POST", "/v1/riders", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    #TODO return boolean 
    return data.decode("utf-8")

def getRider():


def sendRequest(rider, pharmLocation, userLocation):
    

    conn = http.client.HTTPSConnection("api.sparelabs.com")

    payload = "{\n  \"requestedPickupAddress\": \"string\",\n  \"requestedPickupLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"requestedDropoffAddress\": \"string\",\n  \"requestedDropoffLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"estimateId\": \"de5c069b-4ec4-4b77-b171-2dd0db6cdf52\",\n  \"riderId\": \"f6b01ea6-8842-414c-87cc-ee62cc3b997a\",\n  \"numRiders\": 1,\n  \"metadata\": {},\n  \"notes\": \"string\",\n  \"accessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"paymentMethodId\": \"b6df8625-cd25-4123-b345-638aa7b5d011\",\n  \"chargeId\": \"aec0aceb-a4db-49fb-b366-75e90229c640\",\n  \"riders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ]\n}"

    headers = {
        'Content-Type': "application/json",
        'Authorization': ""
        }

    conn.request("POST", "/v1/requests", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    

      
