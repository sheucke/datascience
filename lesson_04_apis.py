import requests
import json

# a sentence we want the sentiment of
sample_sentence = 'A couple hundred hours & several thousand lines of code later...thank you @GA_DC!! #DataScience #GAGradNight'

# we know end URL endpoint to send it to
url = 'http://www.datasciencetoolkit.org/text2sentiment/'

# first we specify the header
header = {'content-type': 'application/json'}

# next we specify the body (the information we want the API to work on)
body = sample_sentence

# now we make the request
response = requests.post(url, data=body, headers=header)

print(response.status_code)
print(response.ok)
print(response.text)
