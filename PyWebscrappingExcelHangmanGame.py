import requests, openpyxl, pandas, random 
from bs4 import BeautifulSoup



def get_url_request():
    # Send a GET request to the URL
    url = "https://www.thenamegeek.com/most-common-first-names"
    request = requests.get(url)
    
    # Check if the request was successful
    if request.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {request.status_code}")
        return
    else:
        return request


def parse_webpage():
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(get_url_request().text, 'html.parser')

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





def get_random_name_from_excel():
    file = "1000Names.xlsx"
    # Read the Excel file
    df = pandas.read_excel(file)
    
    # Check if the DataFrame is not empty and has at least one column with names
    if df.empty or df.shape[1] == 0:
        raise ValueError("Excel file is empty or has no data")
    
    # Assuming the first column contains the names
    name_list = df.iloc[:, 0].tolist()  # Convert the first column to a list
    
    # Select a random name from the list
    random_name = random.choice(name_list)
    
    return random_name

def choose_word():
    return get_random_name_from_excel().lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def guessed_letters():""

def hangman():
    guessed_letters = set()
    attempts_remaining = 5
    while attempts_remaining > 0:
        print("\nWord to guess:", display_word(choose_word(), guessed_letters))
        print("Attempts remaining:", attempts_remaining)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in choose_word():
            print("Good guess!")
            if all(letter in guessed_letters for letter in choose_word()):
                print("\nCongratulations! You guessed the word:", choose_word())
                break
        else:
            print("Wrong guess.")
            attempts_remaining -= 1
    else:
        print("\nGame over! The word was:", choose_word())


#kinda like main function
if __name__ == "__main__":
    #Call scrape_names_to_excel()
    scrape_names_to_excel()
