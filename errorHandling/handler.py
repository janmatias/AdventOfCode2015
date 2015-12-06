import json
import sys

def throw(error):
    errorFile = open("errorHandling/errorCodes.json")
    jsonData = json.load(errorFile)
    errorFile.close()
    print(jsonData[str(error)])
    sys.exit(int(error))

