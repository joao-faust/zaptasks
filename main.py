from dotenv import load_dotenv
load_dotenv()

from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    w = WhatsApp()

    try:
        w.sendMsg()
    except Exception as err:
        print('Error while sending the message')
        print(err)