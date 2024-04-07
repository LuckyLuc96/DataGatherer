import sys
import os
import csv



if len(sys.argv) > 2:
    print('Try: "python csv_reader.py <file_path>"')
    sys.exit(1)
if len(sys.argv) == 2:
    fp = sys.argv[1]
else:
    fp = input('File path: ').strip()
    

with open(fp, 'r') as contents:
    reader = csv.reader(contents)
    rows = []
    for row in reader:
        rows.append(row)


numrows = len(rows)
print("The selected file has", numrows, "rows.")


def row_reader():
    read_row = int(input("Which row would you like to read? "))
    actual_row = read_row - 1 # actual and num rows are so the user can start the count at 1 instead of 0
    num_row = actual_row + 1
    print("Row #1 is {}".format(rows[0]))
    print("Row #{} is {}".format(num_row, rows[actual_row]))
 
    
def search():
    search_entry = input("Search: ")
    results = []
    for search_entry in rows:
        if search_entry != None:
            results.append(search_entry)
            print(results)


def menu():
    user_input = input("What would you like to do? \n 1) Read a specific row. \n 2) Search \n 0) Exit \n  ")
    if user_input.strip() == "1":
      row_reader()
      return True
    if user_input.strip() == "2":
        search()
        return True
    if user_input.strip() == "0":
      return False
      
    else: 
        print("Please enter a number:")
        return True
        
      
while menu():
    pass