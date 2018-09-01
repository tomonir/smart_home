from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

class Appointments(object):

    def __init__(self):
        return
        
    def getAppointments(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        try:
            store = file.Storage('token.json')
            creds = store.get()
            if not creds or creds.invalid:
                flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
                creds = tools.run_flow(flow, store)
            service = build('calendar', 'v3', http=creds.authorize(Http()))

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])
        except:
            print ("Error of geeting appointments.")
        out_put =""
        if not events:
            print('No upcoming events found.')
            return "{'items':["+out_put+"]}"

        for event in events:
            #print (event)
            #print ("----------------------------------------")
            start = event['start'].get('dateTime', event['start'].get('date')) 
            out_put += "{'date':'"+start[0:10]+"',"+ "'time':'"+ start[11:16]+ "'," +"'summary':'"+ event['summary']+"'},"
            #print(start[0:10],start[11:16], event['summary'])
        return "{'items':["+out_put+"]}"


test = Appointments()
print (test.getAppointments())
