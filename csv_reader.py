from tkinter import filedialog
import csv


fp = filedialog.askopenfilename(title="Pick your poison", filetypes=[("csv", "*.csv")])
if not fp:
    print("No file selected.")
else:
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
      menu()
    if user_input.strip() == "2":
        search()
        menu()
    if user_input.strip() == "0":
      return
      
    else: 
        print("Please enter a number:")
        menu()
        
      
menu()