from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement 
from qrcodeT import qrcodeT
from os import environ, getcwd, path
from datetime import datetime
from time import sleep


class WhatsApp:

    def __init__(self, config: dict):
        self.__browser = self.__getChromeInstance()
        self.__config = config

    def __getChromeInstance(self):
        service = Service(ChromeDriverManager().install())

        options = Options()
        # Keeps the user session
        dir_path = getcwd()
        profile = path.join(dir_path, 'profile', 'wpp')
        options = Options()
        options.add_argument(
            r"user-data-dir={}".format(profile))
        # Keeps Chrome opened
        # options.add_experimental_option('detach', True)
        # Runs Chrome without open it
        options.add_argument('--headless')

        return Chrome(service=service, options=options)
    
    def __addLineBreak(self, el: WebElement):
        el.send_keys(Keys.SHIFT + Keys.ENTER)

    def login(self):
        self.__browser.get('https://web.whatsapp.com/')
        # It's necessary to wait because the qrcode isn't rendered immediately
        print('Building Qr Code...')
        sleep(10)
        
        qrCodeEl = self.__browser.find_element(
            'xpath', 
            '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]'
        )
        qrCodeBase64 = qrCodeEl.get_attribute('data-ref')
        qrcodeT(qrCodeBase64)

        print("If you can't connect to WhatsApp Web, try running the script again.")
        print('After connecting to WhatsApp Web you can finish the script execution.')
        print('You have 10 seconds before the browser is closed.')
        sleep(10)
        self.__browser.close()

    def sendEvents(self, events: list|str):
        phoneNumber = str(self.__config['CONTACT_NUMBER'])
        self.__browser.get(f'https://web.whatsapp.com/send?phone={phoneNumber}')
        # It's necessary to wait because WhatsApp isn't opened immediately
        sleep(10)

        inputEl = self.__browser.find_element(
            'xpath',
            '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'
        )
        inputEl.clear()

        if events != 'NO_EVENTS_FOUND':
            for index, event in enumerate(events):
                taskNumber = index+1
                summany = event['summary'] if 'summary' in event else ''
                description = event['description'] if 'description' in event else ''
                startDate = datetime\
                             .fromisoformat(event['start']['dateTime'])\
                             .strftime('%H:%M')
                endDate = datetime\
                           .fromisoformat(event['end']['dateTime'])\
                           .strftime('%H:%M')

                inputEl.send_keys('*EVENTS FOR TODAY*')
                self.__addLineBreak(inputEl)
                self.__addLineBreak(inputEl)
                inputEl.send_keys(f'*{taskNumber} - {summany}({startDate}h-{endDate}h)*')
                self.__addLineBreak(inputEl)
                inputEl.send_keys(f'{description}')
                # If the task isn't the last one then add a line break
                if taskNumber < len(events):
                    self.__addLineBreak(inputEl)
        else:
            inputEl.send_keys('*NO EVENTS FOUND FOR TODAY*')

        inputEl.send_keys(Keys.ENTER)
        # It's necessary to wait a few seconds in order to send the message before 
        # closing the browser
        sleep(10)