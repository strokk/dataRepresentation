from __future__ import print_function
from xlwt import *
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    response = service.users().messages().list(userId='me').execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me', pageToken=page_token).execute()
        messages.extend(response['messages'])

    #creating a workbook
    w = Workbook()
    ws = w.add_sheet('gmail')
    rowNumber = 0;
    ws.write(rowNumber,0,"Subject")
    ws.write(rowNumber,1,"From")
    rowNumber += 1

    for message in messages:

        completeMessage = service.users().messages().get(userId='me', id=message['id']).execute()
        #print(completeMessage)
        headers = completeMessage['payload']['headers']
        subjectHeader = list(filter(lambda h: h['name']=='Subject', headers))[0]['value']
        messageFrom = list(filter(lambda h: h['name']=='From', headers))[0]['value']
        #print(subjectHeader)
        #print(messageTo)
        #print(messageFrom)
        ws.write(rowNumber,0,subjectHeader)
        ws.write(rowNumber,1,messageFrom)
        rowNumber += 1    
    
    w.save('gmail.xls')

    with open('aMessage.json', 'w') as f:
        json.dump(completeMessage, f, indent=4)

if __name__ == '__main__':
    main()


