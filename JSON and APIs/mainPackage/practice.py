# main.py

import requests
import json
from iterateOverADictionaryPackage.iterateOverADictionary import *

# make a request to a web server and store the results in response
response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=LF7AWzCRisZrPqDcUPDGBRRafPqwRwIBcNgzPJLO')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
print(parsed_json)
print(parsed_json['close_approach_data'][0]['relative_velocity'])
#print(parsed_json['data'][0]['directionsInfo'])
    
# total = int(parsed_json['total'])        # The number of parks that were returned
# modify the code to get just the descriptions   
print("The speeds taken for asteroid # 3542519 are:")
for asteroid in parsed_json['close_approach_data']:
    print(asteroid["relative_velocity"])

# invoke the function from the other module, pass it parsed_json

# iterate_dictionary(parsed_json)