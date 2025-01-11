from dotenv import dotenv_values
config = dotenv_values('./.env')

from app.Calendar import Calendaer
from app.WhatsApp import WhatsApp

if __name__ == '__main__':
    try:
        c = Calendaer()
        events = c.getTodaysEvents()
        w = WhatsApp(config)
        w.sendEvents(events)
    except KeyboardInterrupt:
        print('\nBye Bye \U0001F44B')
    except Exception as e:
        print('Error while retrieving the events or sending the message')