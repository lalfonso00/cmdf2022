# import http.client

# conn = http.client.HTTPSConnection("api.sparelabs.com")

# payload = "{\n  \"url\": \"string\",\n  \"types\": [\n    \"requestStatus\"\n  ],\n  \"headers\": [\n    {\n      \"key\": \"string\",\n      \"value\": \"string\"\n    }\n  ]\n}"

# headers = { 'Content-Type': "application/json", 'Authorization':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw" }

# conn.request("POST", "/v1/webhooks", payload, headers)

# res = conn.getresponse()
# data = res.read()
# import http.client

# https://sparelabs-photos.nyc3.digitaloceanspaces.com/Y2VtGMN2thNhj2OkE7zhYuTmLvVAFpFN.jpg
import http.client
import urllib.parse
import json
import datetime
import time
import math
from geopy.geocoders import Nominatim


def addressToLatitudeLongitude(address):
    # Structured Nominatim query may be req for address: https://nominatim.org/release-docs/develop/api/Search
    # locator = geopy.Nominatim()
    # location = locator.geocode("Champ de Mars, Paris, France")

    # address = "90, Park Avenue, New York City, New York, 10016"
    # address = {'street':"4221 Dunbar St"}
    # address = "4221 Dunbar St, Vancouver, Canada"

    geolocator = Nominatim(user_agent="delivery_B")
    location = geolocator.geocode(address, timeout=10, exactly_one=True)
    return location.latitude, location.longitude


def getRiderID(email):
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}
    params = {'email': email}
    conn.request("GET", "/v1/riders?" +
                 urllib.parse.urlencode(params), headers=headers)
    # conn.request("GET", "/v1/riders", headers=headers)

    res = conn.getresponse()
    data = res.read()

    rider = data.decode("utf-8")

    r = json.loads(rider)

    return r["data"][0]["id"]


def createRider():
    # fname = input()
    # lname = input()
    # phoneNum = input()
    # email = input()

    # payload = {'firstName':fname , 'lastName': lname, 'photoUrl': null, 'email': email, 'metadata': {}, 'defaultRiders': }
    payload = "{\n  \"firstName\": \"Lo\",\n  \"lastName\": \"Al\",\n  \"photoUrl\": null,\n  \"phoneNumber\": \"6045559555\",\n  \"email\": \"ljl@gmail.com\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": 3\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    # payload = "{\n  \"firstName\": \"string\",\n  \"lastName\": \"string\",\n  \"photoUrl\": \"string\",\n  \"phoneNumber\": \"string\",\n  \"email\": \"string\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}

    conn.request("POST", "/v1/riders", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    # TODO return boolean
    return data.decode("utf-8")


# def getRider():


def createRequest(riderId, estimateId, requestedDropoffLatitude, requestedDropoffLongitude):
    # email = input()
    # riderid = getRiderID(email)

    # riderid = getRiderID("adam.kobayashi.hrvswa1rng@bot.sparelabs.com")

    conn = http.client.HTTPSConnection("api.sparelabs.com")
    requestedDropoffLongitude

    payloadObj = {'requestedPickupAddress': "string", 'requestedPickupLocation': {'type': "Point", 'coordinates': [
        -123.051335, 49.252176]}, 'requestedDropoffAddress': "string", 'requestedDropoffLocation': {'type': "Point", 'coordinates': [requestedDropoffLongitude, requestedDropoffLatitude]}, 'estimateId': estimateId, 'riderId': riderId}

    payload = json.dumps(payloadObj)
    print("-------------------------------")
    print(payload)
    # payload = "{\n  \"requestedPickupAddress\": \"string " + " \",\n  \"requestedPickupLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"requestedDropoffAddress\": \"string\",\n  \"requestedDropoffLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"estimateId\": \"de5c069b-4ec4-4b77-b171-2dd0db6cdf52\",\n  \"riderId\": \"f6b01ea6-8842-414c-87cc-ee62cc3b997a\",\n  \"numRiders\": 1,\n  \"metadata\": {},\n  \"notes\": \"string\",\n  \"accessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"paymentMethodId\": \"b6df8625-cd25-4123-b345-638aa7b5d011\",\n  \"chargeId\": \"aec0aceb-a4db-49fb-b366-75e90229c640\",\n  \"riders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ]\n}"

    headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}

    conn.request("POST", "/v1/requests", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def getEstimate(svcId, requestedDropoffLatitude, requestedDropoffLongitude):
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    # TODO support user-chosen time
    pickupTime = int(time.time()+300)
    headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}

    # TODO support user-chosen location
    params = {'requestedDropoffLatitude': requestedDropoffLatitude,
              'requestedDropoffLongitude': requestedDropoffLongitude,
              'requestedPickupLatitude': "49.252176",
              'requestedPickupLongitude': "-123.051335",
              'serviceId': svcId,
              'requestedPickupTs': pickupTime}
    conn.request("GET", "/v1/estimates/request?" +
                 urllib.parse.urlencode(params), headers=headers)

    res = conn.getresponse()
    data = res.read()

    estimate = data.decode("utf-8")

    est = json.loads(estimate)
    print("-------------------------------")
    print(est)

    return est["id"]

def getDistance(userLocation, phamarcyLocation):
    return ((userLocation[0]**2 + phamarcyLocation[0]**2) - (userLocation[1]**2 + phamarcyLocation[1]**2))**0.5

def getClosestDistance(userLocations, phamarcyLocations):
    minDistance = math.inf
    distance
    for phamarcyLocation in phamarcyLocations:
        distance = getDistance()
        if()



def getServices(requestedDropoffLatitude, requestedDropoffLongitude):

    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    headers = {'Content-Type': "application/json", 'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMmRmMzBjLWFjMDktNDZhNS05MzI2LWJlZDMzMmY2NzNmMyIsInR5cGUiOiJhcGlLZXkiLCJzZWNyZXQiOiJPb3VucVZsWG1KWFgwMXVaIiwiZXhwaXJlcyI6bnVsbH0.y5DMOdv4YygFhjU7EECo92YrfNLNE_vuKvYExl0ddCiOqP5sYlFNB61ho25etES94SIy_S7wkyKqcAiq_Hxgdw"}
    # 49.252176,-123.051335
    params = {'requestedDropoffLatitude': requestedDropoffLatitude,
              'requestedDropoffLongitude': requestedDropoffLongitude,
              'requestedPickupLatitude': "49.252176",
              'requestedPickupLongitude': "-123.051335"}
    conn.request("GET", "/v1/estimates/services?" +
                 urllib.parse.urlencode(params), headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    service = data.decode("utf-8")

    svc = json.loads(service)
    print(" services \n")
    print(svc)

    return svc["services"][0]["serviceId"]


def main():
    address = input(
        'enter your house number and street name, city, country: ex "4221 Dunbar St, Vancouver, Canada"')

    requestedDropoffLatitude, requestedDropoffLongitude = addressToLatitudeLongitude(
        address)
    print(requestedDropoffLatitude, requestedDropoffLongitude)
    email = input(
        'enter your rider email ex. adam.kobayashi.hrvswa1rng@bot.sparelabs.com')
    riderId = getRiderID(email)
    svcId = getServices(requestedDropoffLatitude, requestedDropoffLongitude)
    estimateId = getEstimate(
        svcId, requestedDropoffLatitude, requestedDropoffLongitude)
    # # print(riderId, estimateId, svcId)
    createRequest(riderId, estimateId, requestedDropoffLatitude,
                  requestedDropoffLongitude)


main()
