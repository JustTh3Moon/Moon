#Reference for using the Google Sheets API
'''
- Videos used: 
https://youtu.be/T1vqS1NL89E
https://youtu.be/bu5wXjz2KvU
- Docs gspread:
https://docs.gspread.org/en/latest/
- How to install pip (And turn a python script into an application:
https://youtu.be/UZX5kH72Yx4
'''
import gspread #pip install gspread

KEY = '1K5aYGuShmjEBBu29Ejns4EbQWWgPfBXCrIE6mO7oeIg' #Spreadsheet ID 

'''
This is the link to the spreadsheet
https://docs.google.com/spreadsheets/d/
1K5aYGuShmjEBBu29Ejns4EbQWWgPfBXCrIE6mO7oeIg  <- this here is the spreadsheet ID
/edit?usp=drivesdk
'''

sa = gspread.service_account(filename="service_account.json") #service account credentials, can be in the same working folder
sh = sa.open_by_key(KEY)

wks = sh.sheet1 #chooses the first sheet to work with
wks = sh.worksheet('Pt1') #Chooses specific sheet to work with 

res = wks.get_all_records() #Gets a dictionary of everything
res = wks.get_all_values() #Gets a list of lists of everything
res = wks.col_values(1) #Gets the first col
res = wks.row_values(1) #Gets the first row
res = wks.get("A3:E3") #Gets the rectangle selected, so A3 to E3 in this example
user = ["crumbIed#3437", "786501915986493450", "too funny", 5, "https://cdn.discordapp.com/avatars/786501915986493450/b48e74e205c927c8e525475cb1d846ae.png?size=4096"] #creates a new user
wks.insert_row(user, 6) #adds the user to the specified row number
wks.append_row(user) #adds the user to the next empty row
wks.update_cell(2, 3, "10- multiple text spams") #updates a cell, removing previous content and replaces it with that
wks.delete_rows(1) #deletes the specified row 
