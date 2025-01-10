from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


class WhatsApp:

    def __init__(self):
        self.__browser = self.__getChromeService()

    def __getChromeService(self):
        service = Service(ChromeDriverManager().install())

        options = Options()
        # Keeps Chrome opened
        options.add_experimental_option('detach', True)
        # Runs Chrome without open it
        # options.add_argument('--headless')

        return Chrome(service=service, options=options)

    def login(self):
        print(self.__browser)