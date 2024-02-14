import json
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    currentTime = datetime.now()
    print("Time at which Lambda invoked" + str(currentTime))
