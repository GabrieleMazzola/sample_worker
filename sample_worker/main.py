from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import request

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/start')
def start():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    driver.get("http://www.google.com")
    return driver.title


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    # TODO: make this async
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
