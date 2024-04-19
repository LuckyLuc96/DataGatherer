from bs4 import BeautifulSoup
import time

def openup(fp):
    with open(fp, 'r') as contents:
        global text
        global soup
        soup = BeautifulSoup(contents, 'html.parser')
        text = soup.get_text()
    html_menu()
        
    
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


def html_menu():
    user_input = input("What would you like to do? \n 1) Show HTML \n 2) Show plain text \n 3) Show links \n 4) Search \n 0) Exit \n  ")
    if user_input.strip() == "1":
        print(soup.prettify())
        print("Scroll up for results.")
        time.sleep(1)
        html_menu()
    if user_input.strip() == "2":
        print(text)
        print("Scroll up for results.")
        time.sleep(1)
        html_menu()
    if user_input.strip() == "3":
        extract_links()
        print("Links with text different past 40 characters not shown.")
        time.sleep(1)
        html_menu()
    if user_input.strip() == "4":
        search()
        time.sleep(1)
        html_menu()
    if user_input.strip() == "0":
        quit()
    else: 
        print("Please enter a valid number:")
        time.sleep(1)
        html_menu()