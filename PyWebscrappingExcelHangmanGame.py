import requests
from bs4 import BeautifulSoup
import openpyxl


def get_url_request():
    # Send a GET request to the URL
    url = "https://www.thenamegeek.com/most-common-first-names"
    request = requests.get(url)
    
    # Check if the request was successful
    if request.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {request.status_code}")
        return
    
    return request


def parse_webpage():
    #Creates response object from the requests class (imported pakckage requests) 
    #only if the status check does NOT equal 200 in get_url_request() function
    response = get_url_request()

    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def find_tags():
    # Find all <a> tags inside <td> elements
    name_elements = parse_webpage().select("td > a")  # CSS selector for <a> inside <td>

    return name_elements


def get_names():
    # Extract text from each element and store it in a list
    names = [name_element.get_text(strip=True) for name_element in find_tags()]

    return names 


def save_names_to_excel():
    # Save the names to an Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Names"

    # Write each name to a new row
    for name in get_names():
        sheet.append([name])

    return workbook


def save_excel_file():
    filename = "1000Names.xlsx"
    # Save the Excel file
    save_names_to_excel().save(filename)
    print(f"Saved {len(get_names())} names to {filename}")

def scrape_names_to_excel():
    #Call get_names function to scrape 
    #the webpage 
    get_names()

    #Call the save_names_to_excel() 
    #function to save scrapped names
    #to the excel file
    save_names_to_excel()

    #Call the save_excel_file() function
    #to save excel file
    save_excel_file()


#kinda like main function
if __name__ == "__main__":
    #Call scrape_names_to_excel()
    scrape_names_to_excel()


