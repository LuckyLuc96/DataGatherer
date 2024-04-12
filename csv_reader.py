import sys
import csv



if len(sys.argv) > 2:
    print('Try: "python csv_reader.py <file_path>"')
    sys.exit(1)
if len(sys.argv) == 2:
    fp = sys.argv[1]
else:
    try:
        fp = input('File path: ').strip()   
    except: 
        print("File not found")
        sys.exit(2) 
    
    

with open(fp, 'r') as contents:
    reader = csv.reader(contents)
    rows = []
    for row in reader:
        rows.append(row)


numrows = len(rows)



def row_reader():
    read_row = int(input("Which row would you like to read? "))
    row_zero = read_row - 1 # "actual" & "num" rows exist so the user can begin at 1 instead of 0
    num_row = row_zero + 1
    print("Row #1 is {}".format(rows[0]))
    print("Row #{} is {}".format(num_row, rows[row_zero]))
 
    
def search():
    search_entry = input("Search: ")
    results = []
    for row in rows:
        for column in row:
            if search_entry.lower() in str(column).lower():
                results.append(row)
                break
    if results:
        print("Search results:")
        for result in results:
            print(results)
    else:
        print("No results found.")


def menu():
    user_input = input("What would you like to do? \n 1) Read a specific row. \n 2) Search \n 0) Exit \n  ")
    if user_input.strip() == "1":
      print("The selected file has", numrows, "rows.")
      row_reader()
      return True
    if user_input.strip() == "2":
        search()
        return True
    if user_input.strip() == "0":
      return False
    else: 
        print("Please enter a valid number:")
        return True
        
   
while menu(): #This starts menu() and also acts as the end of the program once the user returns "0"   
    pass