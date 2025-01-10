from selenium.common.exceptions import NoSuchElementException

from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    whatsApp = WhatsApp()

    try:
        whatsApp.login()
    except Exception as err:
        print('Error to log in or you are already logged in')
        # print(err)