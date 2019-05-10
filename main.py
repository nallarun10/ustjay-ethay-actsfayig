#! usr/bin/ env python3

import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_fact():
    '''Extract random facts from the url using request libary ans get method'''
    '''parse using Beautifulsuop and pull out content'''

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_quote(fact):
    """ the above extracted content need to be entered in box '<form> POST input_text"""

    data = {"input_text": fact}

    r = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", allow_redirects=False, data=data)
    ''' extract the newly formed url'''
    return r.headers['Location']

@app.route('/')
def home():
    fact = get_fact().strip()
    mashup_link = get_quote(fact)
    return mashup_link

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='127.0.0.1', port=port)


