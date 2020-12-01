from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# first run "docker-compose up" to launch the webdrivers
chrome_options = Options()
chrome_options.add_argument("--headless")

drivers = []
for port in [5001, 5002, 5003]:
    drivers.append(
        webdriver.Remote(
            command_executor=f'http://localhost:{port}/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=chrome_options)
    )

drivers[0].get("http://www.google.com")
drivers[0].save_screenshot(f'test0.png')
drivers[1].get("http://www.xtreamers.io")
drivers[0].save_screenshot(f'test1.png')
drivers[2].get("http://www.python.org")
drivers[0].save_screenshot(f'test2.png')

for driver in drivers:
    print(driver.title)

for driver in drivers:
    driver.quit()
