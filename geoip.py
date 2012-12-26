import urllib2, sys
from xml.dom.minidom import parseString

#prepare URL and download the file:
api = 'http://smart-ip.net/geoip-xml/'

query_string = sys.argv[1]

apiurl = api+query_string

file = urllib2.urlopen(apiurl)

data = file.read()

dom = parseString(data)

try:
	countryName = dom.getElementsByTagName("countryName")[0].firstChild.data
except:
	countryName = 'null'

try:
	countryCode = dom.getElementsByTagName("countryCode")[0].firstChild.data
except:
	countryCode = 'null'

try:
	city = dom.getElementsByTagName("city")[0].firstChild.data
except:
	city = 'null'

try:
	longitude = dom.getElementsByTagName("longitude")[0].firstChild.data
except:
	longitude = 'null'
	
try:
	latitude = dom.getElementsByTagName("latitude")[0].firstChild.data
except:
	latitude = 'null'

header="""<MaltegoMessage>
        <MaltegoTransformResponseMessage>
        <Entities>"""
            
footer="""        </Entities>
        </MaltegoTransformResponseMessage> 
    </MaltegoMessage>"""
    
print header

print"""            <Entity Type='maltego.Location'>"""
print"""                  	<Value>%s, %s</Value>""" %(city, countryName)
print"""                    <DisplayInformation>"""
print"""                    </DisplayInformation>"""
print"""					<AdditionalFields>"""
print"""						<Field Name="City" DisplayName="City" MatchingRule="strict">%s</Field>""" %(city)
print"""						<Field Name="Country" DisplayName="Country" MatchingRule="strict">%s</Field>""" %(countryName)
print"""						<Field Name="Country Code" DisplayName="Country Code" MatchingRule="strict">%s</Field>""" %(countryCode)
print"""						<Field Name="Longitude" DisplayName="Longitude" MatchingRule="strict">%s</Field>""" %(longitude)
print"""						<Field Name="Latitude" DisplayName="Latitude" MatchingRule="strict">%s</Field>""" %(latitude)
print"""					</AdditionalFields>"""
print"""			</Entity>"""

print footer