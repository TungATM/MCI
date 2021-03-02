import main
from Google import Create_Service
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pd
import numpy as np
df = main.sql_query
CLIENT_SECRET_FILE = 'test02032020-f96bd03b9833.json'
API_SERVICE_NAME = 'Sheet1'
API_VERSION = 'v4'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1pDgRzqyU6LxG-hahZjKQ658mT26rTk_ku8-BAWNmB9s'
service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
response_date = service.spreadsheets().values().append(
    spreadsheetId=gsheetId,
    valueInputOption='RAW',
    range='DF1!A1',
    body=dict(
        majorDimension='ROWS',
        values=df.T.reset_index().T.values.tolist())
).execute()
#
# # df.to
