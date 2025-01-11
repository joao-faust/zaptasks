from os import path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Calendaer:

    def __init__(self):
        self.__scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        self.__calendar = self.__getCalendarInstance()
    
    def __getCalendarInstance(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if path.exists('token.json'):
            creds = Credentials.from_authorized_user_file(
                'token.json', 
                self.__scopes
            )
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', 
                    self.__scopes
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)
    
    def getTodaysEvents(self) -> list|str:
        today = datetime.now()
        start_of_day = today.replace(
            hour=0, 
            minute=0, 
            second=0, 
            microsecond=0
        ).isoformat() + 'Z'
        end_of_day = today.replace(
            hour=23, 
            minute=59, 
            second=59, 
            microsecond=999999
        ).isoformat() + 'Z'

        events_result = (
            self.__calendar.events()
            .list(
                calendarId='primary',
                timeMin=start_of_day,
                timeMax=end_of_day,
                singleEvents=True,
                orderBy='startTime',
            )
            .execute()
        )
        events = events_result.get('items', [])
        if not events:
            return 'NO_EVENTS_FOUND'
        
        return events
        