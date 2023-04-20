# main.py

import requests
import json
from iterateOverADictionaryPackage.iterateOverADictionary import *

# make a request to a web server and store the results in response
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=LF7AWzCRisZrPqDcUPDGBRRafPqwRwIBcNgzPJLO&query=Cheddar%20Cheese')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
print(parsed_json)
#print(parsed_json['description'][2015943]['gtinUPC'])
#print(parsed_json['data'][0]['directionsInfo'])
    
# total = int(parsed_json['total'])        # The number of parks that were returned
# modify the code to get just the descriptions    
# for park in parsed_json['data']:
#    print (park["description"])

# invoke the function from the other module, pass it parsed_json

iterate_dictionary(parsed_json)
