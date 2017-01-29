import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
      #  print data
        continue

#    print json.dumps(js, indent=4)

    Place_id = js["results"][0]["place_id"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'Place_id', Place_id
 #   location = js['results'][0]['formatted_address']
  #  print location

