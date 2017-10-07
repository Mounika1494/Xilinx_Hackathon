import requests 
import json
import os
import re

url_Microsoft_Cog_Services = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize?'
Image_url = 'Anger.jpg'
#Header for Microsoft Cognitive Services requests
headers = {
    # Request headers #To confirm octet or json
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'a6a9555023d74986a23d4a6935274f88',
}

#Parameters for Microsoft Cognitive Services requests
params =  {
    # Request parameters
    #'visualFeatures':'Description'
}

#Capturing Image of the requested Item
                #os.system('raspistill -q 25 -o /home/pi/Request_Item.jpg')
				#Converting the Image into a readable binary file for passing to the Microsoft Cognitive Services
with open (Image_url, 'rb') as f:
    data2 = f.read()
				#Http Post request to the Microsoft Cognitive Services 	
response= requests.request('post',url_Microsoft_Cog_Services,json =json, data = data2, headers = headers, params = params)
data = response.json()
print(data)
				#Searching for Pattern of the required items in the image response from cognitive services
data1 = json.loads(json.dumps(data['scores'][0]['anger']))
print(data1)

                #Apple_Found = re.search('apple', str(data))
                #Cabbage_Found = re.search('cabbage',str(data))
