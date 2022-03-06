
# https://sparelabs-photos.nyc3.digitaloceanspaces.com/Y2VtGMN2thNhj2OkE7zhYuTmLvVAFpFN.jpg
import http.client
import urllib.parse
import json
import datetime
import time
import os
from geopy.geocoders import Nominatim


def addressToLatitudeLongitude(address):

    geolocator = Nominatim(user_agent="delivery_B")
    location = geolocator.geocode(address, timeout=10, exactly_one=True)
    return location.latitude, location.longitude


def getRiderID(email, API_KEY):
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}
    params = {'email': email}
    conn.request("GET", "/v1/riders?" +
                 urllib.parse.urlencode(params), headers=headers)

    res = conn.getresponse()
    data = res.read()

    rider = data.decode("utf-8")

    r = json.loads(rider)
    # print(r["data"][0]["id"])

    return r["data"][0]["id"]


def createRider(API_KEY):
    fname = input('enter your first name')
    lname = input('enter your last name')
    phoneNum = input('enter your phone number')
    email = input('enter your email')
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # payloadObj = {'firstName': fname, 'lastName': lname, 'photoUrl': null, 'phoneNumber': phoneNum, 'email': email, 'metadata' {}, 'defaultRiders':[{'type': "adult",'count': 1 }], 'defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": 3\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}" }

    # payload = {'firstName':fname , 'lastName': lname, 'photoUrl': null, 'email': email, 'metadata': {}, 'defaultRiders': }
    payload = "{\n  \"firstName\": \"" + fname + "\",\n  \"lastName\": \"" + lname + ",\n  \"photoUrl\": null,\n  \"phoneNumber\": \"" + phoneNum + "\",\n  \"email\": \"" + email + \
        "\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": 3\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    # payload = "{\n  \"firstName\": \"string\",\n  \"lastName\": \"string\",\n  \"photoUrl\": \"string\",\n  \"phoneNumber\": \"string\",\n  \"email\": \"string\",\n  \"metadata\": {},\n  \"defaultRiders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ],\n  \"defaultAccessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"defaultNotes\": \"string\"\n}"
    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}

    conn.request("POST", "/v1/riders", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    # TODO return boolean
    return data.decode("utf-8")


# def getRider():


def createRequest(riderId, estimateId, requestedDropoffLatitude, requestedDropoffLongitude, API_KEY):
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

    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}

    conn.request("POST", "/v1/requests", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def getEstimate(svcId, requestedDropoffLatitude, requestedDropoffLongitude, API_KEY):
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    # TODO support user-chosen time
    pickupTime = int(time.time()+300)
    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}

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


def getServices(requestedDropoffLatitude, requestedDropoffLongitude, API_KEY):

    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}
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
    API_KEY = os.getenv('SPARE_LABS_KEY')
    address = input(
        'enter your house number and street name, city, country: ex "4221 Dunbar St, Vancouver, Canada"')

    requestedDropoffLatitude, requestedDropoffLongitude = addressToLatitudeLongitude(
        address)
    print(requestedDropoffLongitude, ",", requestedDropoffLatitude)

    email = input(
        'enter your rider email ex. adam.kobayashi.hrvswa1rng@bot.sparelabs.com')
    riderId = getRiderID(email, API_KEY)
    svcId = getServices(requestedDropoffLatitude,
                        requestedDropoffLongitude, API_KEY)
    estimateId = getEstimate(
        svcId, requestedDropoffLatitude, requestedDropoffLongitude, API_KEY)
    print(riderId, estimateId, svcId)
    createRequest(riderId, estimateId, requestedDropoffLatitude,
                  requestedDropoffLongitude, API_KEY)


main()
