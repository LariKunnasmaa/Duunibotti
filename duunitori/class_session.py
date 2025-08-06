from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class SeleniumSession():
    """
    Session class for managing a Selenium Firefox WebDriver session.
    For easier navigation and interaction with web pages.
    Methods
    -------
    __init__(geckodriver_path=None)
        Initializes the Firefox WebDriver with the specified geckodriver path.
    open_url(url)
        Opens the specified URL in the browser.
    xpath(xpath)
        Waits for and returns a single visible element located by the given XPath.
    xpaths(xpath)
        Waits for and returns all visible elements located by the given XPath.
    click(xpath)
        Waits for and clicks a visible element located by the given XPath.
    """
    
    
    def __init__(self, geckodriver_path=None):
        service = Service(geckodriver_path)
        self.driver = webdriver.Firefox(service=service)

    def open_url(self, url):
        self.driver.get(url)

    def xpath(self, xpath):
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element
    
    def xpaths(self, xpath):
        elements =  WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        return elements
    
    def click(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
    

def init_session(path =r"c:\Python\New folder (2)\geckodriver.exe" ):
    session = SeleniumSession(path)
    return session
