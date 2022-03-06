
# https://sparelabs-photos.nyc3.digitaloceanspaces.com/Y2VtGMN2thNhj2OkE7zhYuTmLvVAFpFN.jpg
import http.client
import urllib.parse
import json
import datetime
import time
import os
import math
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


def createRequest(riderId, estimateId, requestedDropoffLatitude, requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY):
    # email = input()
    # riderid = getRiderID(email)

    # riderid = getRiderID("adam.kobayashi.hrvswa1rng@bot.sparelabs.com")

    conn = http.client.HTTPSConnection("api.sparelabs.com")
    requestedDropoffLongitude

    payloadObj = {'requestedPickupAddress': "string", 'requestedPickupLocation': {'type': "Point", 'coordinates': [
        requestedPickupLongitude, requestedPickupLatitude]}, 'requestedDropoffAddress': "string", 'requestedDropoffLocation': {'type': "Point", 'coordinates': [requestedDropoffLongitude, requestedDropoffLatitude]}, 'estimateId': estimateId, 'riderId': riderId}

    payload = json.dumps(payloadObj)
    print("-------------------------------")
    # print(payload)
    # payload = "{\n  \"requestedPickupAddress\": \"string " + " \",\n  \"requestedPickupLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"requestedDropoffAddress\": \"string\",\n  \"requestedDropoffLocation\": {\n    \"type\": \"Point\",\n    \"coordinates\": [\n      -180,\n      -180\n    ]\n  },\n  \"estimateId\": \"de5c069b-4ec4-4b77-b171-2dd0db6cdf52\",\n  \"riderId\": \"f6b01ea6-8842-414c-87cc-ee62cc3b997a\",\n  \"numRiders\": 1,\n  \"metadata\": {},\n  \"notes\": \"string\",\n  \"accessibilityFeatures\": [\n    {\n      \"type\": \"wheelchair\",\n      \"count\": \"\"\n    }\n  ],\n  \"paymentMethodId\": \"b6df8625-cd25-4123-b345-638aa7b5d011\",\n  \"chargeId\": \"aec0aceb-a4db-49fb-b366-75e90229c640\",\n  \"riders\": [\n    {\n      \"type\": \"adult\",\n      \"count\": 1\n    }\n  ]\n}"

    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}

    conn.request("POST", "/v1/requests", payload, headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    print("your Plan C delivery has been created and a Driver is on the way!")


def getEstimate(svcId, requestedDropoffLatitude, requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY):
    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    # TODO support user-chosen time
    pickupTime = int(time.time()+300)
    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}

    # TODO support user-chosen location
    params = {'requestedDropoffLatitude': requestedDropoffLatitude,
              'requestedDropoffLongitude': requestedDropoffLongitude,
              'requestedPickupLatitude': requestedPickupLatitude,
              'requestedPickupLongitude': requestedPickupLongitude,
              'serviceId': svcId,
              'requestedPickupTs': pickupTime}
    conn.request("GET", "/v1/estimates/request?" +
                 urllib.parse.urlencode(params), headers=headers)

    res = conn.getresponse()
    data = res.read()

    estimate = data.decode("utf-8")

    est = json.loads(estimate)
    print("-------------------------------")
    # print(est)
    print("estimate confirmed!")

    return est["id"]


def getDistance(userLocation, phamarcyLocation):
    return ((userLocation[0]**2 + phamarcyLocation[0]**2) - (userLocation[1]**2 + phamarcyLocation[1]**2))**0.5


def getClosestDistance(userLocation, phamarcyLocations):
    minDistance = math.inf
    for phamarcyLocation in phamarcyLocations:
        distance = getDistance(userLocation, phamarcyLocation)
        # print(distance)
        if(distance < minDistance):
            minDistance = distance
            closestPhamarcyLocation = phamarcyLocation
            # print(minDistance)
    return closestPhamarcyLocation


def getServices(requestedDropoffLatitude, requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY):

    conn = http.client.HTTPSConnection("api.sparelabs.com")

    # conn.request("GET", "/v1/estimates/request", headers=headers)

    headers = {'Content-Type': "application/json",
               'Authorization': "Bearer " + API_KEY}
    # 49.252176,-123.051335
    params = {'requestedDropoffLatitude': requestedDropoffLatitude,
              'requestedDropoffLongitude': requestedDropoffLongitude,
              'requestedPickupLatitude': requestedPickupLatitude,
              'requestedPickupLongitude': requestedPickupLongitude}
    conn.request("GET", "/v1/estimates/services?" +
                 urllib.parse.urlencode(params), headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    service = data.decode("utf-8")

    svc = json.loads(service)
    print(" services \n")
    # print(svc)
    print("service confirmed!")

    return svc["services"][0]["serviceId"]


def main():
    pharmacies = [[-123.122167, 49.2834485],
                  [-123.06887366948149, 49.2626459],
                  [-123.1853879, 49.2321965],
                  [-123.1178585, 49.2335447],
                  [-123.0900995, 49.2501799],
                  [-123.06887366948149, 49.2626459],
                  [-123.057168, 49.2411628],
                  [-123.001045, 49.2680839],
                  [-123.139408, 49.2855264],
                  [-123.1159099, 49.2635864]]

    API_KEY = os.getenv('SPARE_LABS_KEY')
    address = input(
        'enter your house number and street name, city, country: ex "4221 Dunbar St, Vancouver, Canada"')

    requestedDropoffLatitude, requestedDropoffLongitude = addressToLatitudeLongitude(
        address)
    # print(requestedDropoffLongitude, ",", requestedDropoffLatitude)
    userLocation = [requestedDropoffLongitude, requestedDropoffLatitude]
    # print(userLocation)
    pharmacyLocation = getClosestDistance(userLocation, pharmacies)
    requestedPickupLongitude = pharmacyLocation[0]
    requestedPickupLatitude = pharmacyLocation[1]

    # createRider(API_KEY)
    email = input(
        'enter your rider email ex. adam.kobayashi.hrvswa1rng@bot.sparelabs.com')
    riderId = getRiderID(email, API_KEY)
    svcId = getServices(requestedDropoffLatitude,
                        requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY)
    estimateId = getEstimate(
        svcId, requestedDropoffLatitude, requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY)
    print(riderId, estimateId, svcId)
    createRequest(riderId, estimateId, requestedDropoffLatitude,
                  requestedDropoffLongitude, requestedPickupLatitude, requestedPickupLongitude, API_KEY)


main()
