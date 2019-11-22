import requests  # how python gets webpages
from bs4 import BeautifulSoup  # Creates structured, seachable object
import pandas as pd
import matplotlib.pyplot as plt

# First, let's play with beautiful soup on a "toy" webpage

html_doc = """
<!doctype html>

<html lang="en">
<head>
  <title>Brandon's Homepage!</title>
</head>

<body>
  <h1>Brandon's Homepage</h1>
  <p id="intro">My name is Brandon.  I'm love web scraping!</p>
  <p id="background">I'm originally from Louisiana.  I went to undergrad at Louisiana Tech and grad school at UNC.</p>
  <p id="current">I currently work as a Product Manager of Linguistics and Analytics at Clarabridge.</p>
  
  <h3>My Hobbies</h3>
  <ul>
      <li id="my favorite">Data Science</li>
      <li>Backcountry Camping</li>
      <li>Rock Climbing</li>
      <li>Cycling</li>
      <li>The Internet</li>
  </ul>
</body>
</html>
"""
