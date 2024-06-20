from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = ""
endpoint = ""

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

logo = "https://raw.githubusercontent.com/axel-sirota/getting-started-azure-computer-vision/main/Images/my_car.jpg"

brand_response = computervision_client.analyze_image(logo, visual_features=["Brands"], max_candidates=1)

print(brand_response)
