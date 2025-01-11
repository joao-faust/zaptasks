from dotenv import load_dotenv
load_dotenv()

from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    whatsApp = WhatsApp()

    try:
        whatsApp.login()
    except KeyboardInterrupt:
        print('\nBye Bye \U0001F44B')
    except Exception as err:
        print('Error while logging in or you are already logged in')