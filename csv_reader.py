import csv
import statistics

def openup(fp):
    global rows
    global numrows
    with open(fp, 'r') as contents:
        reader = csv.reader(contents)
        rows = []
        for row in reader:
            converted_row = [float(val) if val.replace('.', '', 1).isdigit() else val for val in row]
            rows.append(converted_row)
    numrows = len(rows)
    csv_menu()

def row_reader():
    read_row = int(input("Which row would you like to read? "))
    row_zero = read_row - 1 # "read_row" & "row_zero" exist so the user can begin at 1 instead of 0
    num_row = row_zero + 1
    print("Row #1 is {}".format(rows[0]))
    print("Row #{} is {}".format(num_row, rows[row_zero]))
 
def get_num_column():
    column_counter = 0
    for item in rows[0]:
        column_counter = column_counter + 1
    print("There are", column_counter, "columns and", numrows, "rows.")

def math_menu():
    input_math_menu = input('Would you like to perform operations on a column or a row? \n Enter "A" for columns \n Enter "B" for rows \n Enter "0" to exit\n').upper()
    if input_math_menu == "A":
        column_math()
        math_menu()
    if input_math_menu == "B":
        row_math()
        math_menu()
    if input_math_menu == "0":
        quit()
    else:
        print("Invalid input")
        math_menu()
    
def column_math():
    get_num_column()
    print("This is column_math and isn't implimented yet")
    
def row_math():
    get_num_column()
    input_row = int(input("Which row would you like to perform operations on?\n"))
    row_value = rows[input_row - 1]
    numeric_values = [float(value) for value in row_value if isinstance(value, float)]
    try:
        print("Peforming math operations on row", input_row)
        print("The sum of all numbers in this row is: ", sum(numeric_values))
        print("The mean of all numbers in this row is: ", statistics.mean(numeric_values))
        print("The median of all numbers in this row is: ", statistics.median(numeric_values))
        print()
    except IndexError:
        print("Invalid row number")
    except Exception as e:
        print("An error occured:", e)
        

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


def csv_menu():
    user_input = input("What would you like to do? \n 1) Read a specific row. \n 2) Search \n 3) Do math \n 0) Exit \n  ")
    if user_input.strip() == "1":
      print("The selected file has", numrows, "rows.")
      row_reader()
      csv_menu()
    if user_input.strip() == "2":
        search()
        csv_menu()
    if user_input.strip() == "3":
        math_menu()
        csv_menu()
    if user_input.strip() == "0":
        quit()
    else: 
        print("Please enter a valid number, such as '1' or '0'")
        csv_menu()