#Reference for using the Google Sheets API
import gspread

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("1mSq881EYr4a5z3wpD8OyZl_jdJagwYuQexmYN1szLOI")

wks = sh.sheet1

res = wks.get_all_records() #Gets a dictionary of everything
res = wks.get_all_values() #Gets a list of lists of everything
res = wks.col_values(1) #Gets the first col
res = wks.row_values(1) #Gets the first row
res = wks.get("A3:E3") #Gets the rectangle selected, so A3 to E3 in this example
user = ["crumbIed#3437", "786501915986493450", "5-nsfw pfp", 5, "https://cdn.discordapp.com/avatars/786501915986493450/b48e74e205c927c8e525475cb1d846ae.png?size=4096"] #creates a new user
wks.insert_row(user, 6) #adds the user to the specified row number
wks.append_row(user) #adds the user to the next empty row
wks.update_cell(2, 3, "10- multiple text spams") #updates a cell, removing previous content and replaces it with that
wks.delete_rows(1) #deletes the specified row 
