from pprint import pprint
import googlemaps

API_KEY = ''

map_client = googlemaps.Client(API_KEY)

landmark1 = 'Piata Arcul de Triumf, Bucuresti'
response = map_client.geocode(landmark1)
pprint(response)
print(response[0]['geometry'])
