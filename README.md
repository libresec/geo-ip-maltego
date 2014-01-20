# About 

GeoIP resolution transform for smart-ip.net. Accepts 
an ip address or domain name as a command line argument 
and returns the geoip information. 

# Install

Import into Maltego and run it on an ip address or domain
name entity.

# Usage

```

$python geoip.py [argument]

```

# Dependencies

To generate the transform XML, this includes MaltegoTransform-py
from Paterva.

- http://www.paterva.com/web6/documentation/MaltegoTransform-Python.zip

HTTP requests require the requests module.

- http://docs.python-requests.org/en/latest/
