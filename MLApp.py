import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'AVGHEARTBEATSPERMIN': "93",   
                            'PALPITATIONSPERDAY': "22",   
                            'CHOLESTEROL': "163",   
                            'BMI': "25",   
                            'AGE': "49",   
                            'SMOKERLAST5YRS': "N",   
                            'EXERCISEMINPERWEEK': "110",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/e293e69595da4913a5ba4bb8bdc439a8/services/1df4e41d9fe6467e9ffcc2814d73f748/execute?api-version=2.0&format=swagger'
api_key = '6N2NLKFuV7HCGXzCuHslPlHVuxSJKPxjeihSY2hPRhEcYXxB8LfmziygDuUoguMHyhfEDl3IU1CA+4NJumc76g==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))