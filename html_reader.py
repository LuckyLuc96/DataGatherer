from bs4 import BeautifulSoup
from main import fpvalue

fp = fpvalue
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
            print(result,'\n')
    else:
        print("No results found.")
        
def extract_links():
    links = set()
    for link in soup.find_all('a', href=True):
        link_text=link['href']
        link_text = link_text[:39] #Truncate the link to the first 40 characters to remove very similar links
        links.add(link_text)
    for items in links:
        print(items, '\n')


def menu():
    user_input = input("What would you like to do? \n 1) Show HTML \n 2) Show plain text \n 3) Show links \n 4) Search \n 0) Exit \n  ")
    if user_input.strip() == "1":
        print(soup.prettify())
        print("Scroll up for results.")
        return True
    if user_input.strip() == "2":
        print(text)
        print("Scroll up for results.")
        return True 
    if user_input.strip() == "3":
        extract_links()
        print("Links with text different past 40 characters not shown.")
        return True
    if user_input.strip() == "4":
        search()
        return True
    if user_input.strip() == "0":
      return False
    else: 
        print("Please enter a valid number:")
        return True
        
   
while menu(): #This starts menu() and also acts as the end of the program once the user returns "0"   
    pass