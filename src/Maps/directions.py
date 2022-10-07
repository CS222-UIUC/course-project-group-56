import urllib.request
import json
import time
import datetime
dir_key = "AIzaSyDHLd5Un37rDvM2S0-BUElvXWgme-BhQus"
geo_key = "AIzaSyD7JSgFmErSLWKaJNlYGD_V3LkmDbcuqyQ"
dir_call = "https://maps.googleapis.com/maps/api/directions/json?"
geo_call = "https://www.googleapis.com/geolocation/v1/geolocate?key="
origin = "106 e daniel st, champaign, IL".replace(" ","+")
destination = "campus instructional facility".replace(" ","+")
method = "driving"
class_time = 1664465400
req = "origin={}&destination={}&mode={}&arrival_time={}&key={}".format(origin, destination, method, class_time, dir_key)
response = urllib.request.urlopen(dir_call+req).read()
directions = json.loads(response)
routes = directions['routes']
legs = routes[0]['legs']
traveltime = legs[0]['duration']['text']
