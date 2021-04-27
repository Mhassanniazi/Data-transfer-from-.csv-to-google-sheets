import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
client = gspread.authorize(credentials)

googlesheet=input("Please Enter the GOOGLE SHEET NAME: ")
spreadsheet = client.open(googlesheet)

csv=input("PLease Enter the .csv File name: ")+'.csv'
with open(csv, 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)
    print("DATA SUCCESSFULLY TRANSFERED")
    


























