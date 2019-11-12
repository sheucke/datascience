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

# turn the text in json
r_json = json.loads(response.text)
print(r_json)
print(r_json['score'])


def get_sentiment(text):
    url = 'http://www.datasciencetoolkit.org/text2sentiment/'

    # specify header
    header = {'content-type': 'application/json'}

    # Next we specify the body (the information we want the API to work on)
    body = text

    # Now we make the request
    response = requests.post(url, data=body, headers=header)
    # Notice that this is a POST request
    r_json = json.loads(response.text)
    sentiment = r_json['score']  # 2.0
    return sentiment


sentences = ['I love pizza!', 'I hate pizza!', 'I feel nothing about pizza!']

# loop through the sentences
for sentence in sentences:
    sentiment = get_sentiment(sentence)
    print(sentence, sentiment)
