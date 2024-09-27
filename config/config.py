
"""
BROWSER (str): The browser to be used for running tests. Default is "chrome".
URL (str): The base URL of the application under test. Default is the SauceDemo site.
HEADLESS (bool): Whether to run the browser in headless mode. Default is False.
MOBILE (bool): Whether to simulate a mobile device. If True, DEVICE_NAME must be specified. 
               Default is True.
DEVICE_NAME (str): The device name to be used when simulating a mobile device (e.g., 'iPhone X', 
                   'Pixel 4'). Default is 'iPhone X'.
LOG_LEVEL (str): The logging level for the test execution (e.g., DEBUG, INFO, WARNING, ERROR).
                 Default is "DEBUG".
LOG_NAME (str): The name of the log file to store logs. Default is "log_file.log".
USER_USERNAME (str): The username for login during tests. Default is 'standard_user'.
USER_PASSWORD (str): The password for login during tests. Default is 'secret_sauce'.
"""
import os


BROWSER = "chrome"
URL = "https://www.saucedemo.com/"
HEADLESS = os.environ.get('HEADLESS', 'False').lower() == 'true'
MOBILE = True
DEVICE_NAME = "iPhone X"
LOG_LEVEL = "DEBUG"
LOG_NAME = "log_file.log"
USER_USERNAME = os.getenv("USER_USERNAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")

if not USER_USERNAME or not USER_PASSWORD:
    raise EnvironmentError("Environment variables USER_USERNAME and USER_PASSWORD must be set")
