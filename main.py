from dotenv import load_dotenv
load_dotenv()

from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    w = WhatsApp()
    w.sendMsg()
    print('Hello world from zaptasks')