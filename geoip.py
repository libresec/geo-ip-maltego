'''
geoipMaltego is a Maltego transform that will retrieve
geoip information from the smart-ip.net json API.

'''
from __future__ import print_function
from MaltegoTransform import *
import requests
import sys

api = 'http://smart-ip.net/geoip-json/'
ip = sys.argv[1]
transform = MaltegoTransform()

try:
    response = requests.get(api + ip)
except requests.exceptions.RequestException as e:
    transform.addException(str(e))
    transform.throwExceptions()

if response.headers['content-type'] == 'application/json':
    d = response.json()

    if not 'error' in d:
        location = [
            d.get('city', 'null'),
            d.get('region', 'null'),
            d.get('countryName', 'null')
            ]
    else:
        location = ['error']

    entity = transform.addEntity('maltego.Location', ','.join(location))

    for k, v in response.json().iteritems():
        entity.addAdditionalFields(k, k, True, v)

    transform.returnOutput()
