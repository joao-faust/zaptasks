from dotenv import load_dotenv
load_dotenv()
from selenium.common.exceptions import NoSuchElementException

from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    whatsApp = WhatsApp()

    try:
        whatsApp.login()
    except Exception as err:
        print(err)
        print('Error to log in or you are already logged in')