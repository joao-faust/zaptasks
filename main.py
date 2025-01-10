from dotenv import load_dotenv
load_dotenv()

from app.Calendar import Calendaer
from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    try:
        c = Calendaer()
        events = c.getTodaysEvents()
        w = WhatsApp()
        w.sendEvents(events)
    except Exception as e:
        print('Error while retrieving the events or sending the message')