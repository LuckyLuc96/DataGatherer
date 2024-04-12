from bs4 import BeautifulSoup


fp = "/home/lucky1/Documents/My Games/Programs/Python/csv_reader/example.html"
with open(fp, 'r') as contents:
    soup = BeautifulSoup(contents, 'html.parser')
    text = soup.get_text()




 
    
def search():
    search_entry = input("Search: ")
    results = []
    for line in text.split('\n'):
        if search_entry.lower() in line.lower():
            results.append(line.strip())
    if results:
        print("Search results:")
        for result in results:
            print(result)
    else:
        print("No results found.")


def menu():
    user_input = input("What would you like to do? \n 1) Show HTML \n 2) Show plain text \n 3) Search \n 0) Exit \n  ")
    if user_input.strip() == "1":
        print(soup.prettify())
        print("Scroll up for results.")
        return True
    if user_input.strip() == "2":
        print(text)
        print("Scroll up for results.")
        return True 
    if user_input.strip() == "3":
        search()
        return True
    if user_input.strip() == "0":
      return False
    else: 
        print("Please enter a valid number:")
        return True
        
   
while menu(): #This starts menu() and also acts as the end of the program once the user returns "0"   
    pass