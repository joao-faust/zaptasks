from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from qrcodeT import qrcodeT
from os import getenv
from time import sleep


class WhatsApp:

    def __init__(self):
        self.__browser = self.__getChromeInstance()

    def __getChromeInstance(self):
        service = Service(ChromeDriverManager().install())

        options = Options()
        # Keeps the user session
        options.add_argument('--user-data-dir=./User_Data')
        # Keeps Chrome opened
        # options.add_experimental_option('detach', True)
        # Runs Chrome without open it
        # options.add_argument('--headless')

        return Chrome(service=service, options=options)

    def login(self):
        self.__browser.get('https://web.whatsapp.com/')
        # It's necessary to wait because the qrcode isn't rendered immediately
        print('Building Qr Code...')
        sleep(15)
        
        qrCodeEl = self.__browser.find_element(
            'xpath', 
            '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]'
        )
        qrCodeBase64 = qrCodeEl.get_attribute('data-ref')
        qrcodeT(qrCodeBase64)

        print('You have 20 seconds to log in')
        sleep(20)
        self.__browser.close()

    def sendMsg(self):
        phoneNumber = str(getenv('PHONE_NUMBER'))
        self.__browser.get(f'https://web.whatsapp.com/send?phone={phoneNumber}')
        # It's necessary to wait because WhatsApp isn't opened immediately
        sleep(15)

        inputEl = self.__browser.find_element(
            'xpath',
            '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'
        )
        inputEl.send_keys('teste')
        inputEl.send_keys(Keys.ENTER)