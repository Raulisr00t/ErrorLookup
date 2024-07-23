# Microsoft Windows Error Lookup
This project is a PyQt5 application for looking up Microsoft Windows system error codes (0-499). It retrieves error codes and descriptions from the Microsoft documentation and provides an easy-to-use graphical interface for users to search for specific error codes.

## Features
Fetch Error Codes: Retrieves error codes and their descriptions from the Microsoft documentation.
Search Functionality: Allows users to input an error number and get the corresponding error code and description.
Graphical User Interface (GUI): Built using PyQt5, offering a user-friendly interface for easy interaction.

## Requirements
Python 3.x
PyQt5
Requests
BeautifulSoup4

### Installation
Clone the Repository:
```sh
git clone https://github.com/Raulisr00t/ErrorLookup.git
cd ./ErrorLookup
```
Install Dependencies:
pip install requests beautifulsoup4 PyQt5

### Usage
Run the Application:
```powershell
python3 ErrorLookup.py
```
Using the Application:
Enter the error number in the input field.
Click the "Search" button to retrieve the error code and description.
The result will be displayed in the text area below.

### Code Explanation
error_lookup.py
This script contains the main application code.

ErrorLookupApp Class
This class inherits from QWidget and sets up the PyQt5 GUI. Key components include:

QLineEdit for entering the error number.
QPushButton for triggering the search.
QTextEdit for displaying the result.
initUI Method
Initializes the user interface, sets up the layout, and adds widgets.

lookup_error Method
Handles the search functionality:

Retrieves the error number from the input field.
Checks if the error number exists in the dictionary.
Displays the corresponding error code and message.
fetch_error_codes Function
Fetches error codes and their descriptions from the Microsoft documentation:

Uses requests to get the webpage content.
Parses the content with BeautifulSoup.
Extracts error codes, numbers, and messages and stores them in a dictionary.

#### Main Block
Fetches the error codes and initializes the PyQt5 application.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
PyQt5 Documentation
Requests Library
BeautifulSoup Documentation
