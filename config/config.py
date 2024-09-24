
"""
A configuration class for setting up the browser and test environment.

BROWSER (str): The browser to be used for running tests. Default is "chrome".
URL (str): The base URL of the application under test. Default is the Twitch mobile site.
DEVICE_NAME (str): The device name to be used to simulate a mobile. (e.g. 'iPhone SE', 
                    'iPhone 12 Pro', 'Pixel 4', 'Nexus 6')
LOG_LEVEL (str): The level of logging to be used (e.g., DEBUG, INFO). Default is "DEBUG".
LOG_NAME (str): The name of the log file.
"""

BROWSER = "chrome"
URL = "https://www.saucedemo.com/"
HEADLESS = False
MOBILE = True
DEVICE_NAME = "iPhone X"
LOG_LEVEL = "DEBUG"
LOG_NAME = "log_file.log"
USER_USERNAME = "standard_user"
USER_PASSWORD = "secret_sauce"
