from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/start')
def start():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    driver.get("http://www.python.org")
    return driver.page_source


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
