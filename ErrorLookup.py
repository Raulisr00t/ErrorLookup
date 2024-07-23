import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class ErrorLookupApp(QWidget):
    def __init__(self, error_dict):
        super().__init__()
        self.error_dict = error_dict
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Error Lookup")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        grid = QGridLayout()

        self.error_input = QLineEdit(self)
        self.error_input.setPlaceholderText("Enter Error Number")

        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.lookup_error)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)

        grid.addWidget(QLabel("Error Number:"), 0, 0)
        grid.addWidget(self.error_input, 0, 1, 1, 2)
        grid.addWidget(self.search_button, 1, 1)
        grid.addWidget(self.result_area, 2, 0, 1, 3)

        layout.addLayout(grid)
        self.setLayout(layout)

    def lookup_error(self):
        error_number = self.error_input.text().strip()
        if error_number.lower() in ('exit', 'quit'):
            self.close()
            return
        
        if not error_number:
            return ""
        
        if error_number in self.error_dict:
            error_code, error_message = self.error_dict[error_number]
            self.result_area.setText(f"{error_code}: {error_message}")
        
        else:
            self.result_area.setText("Your error cannot be found!")

def fetch_error_codes():
    site = "https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-"
    try:
        response = requests.get(url=site, allow_redirects=False)
        response.raise_for_status()  
        content = response.text
        html = BeautifulSoup(content, "html.parser")
        
        error_dict = {}
        
        p_tags = html.find_all('p')
        
        i = 0
        while i < len(p_tags):
            strong_tag = p_tags[i].find('strong')
            if strong_tag:
                error_code = strong_tag.text.strip()
                error_number = p_tags[i+1].text.split()[0].strip()
                error_message = p_tags[i+2].text.strip()
                error_dict[error_number] = (error_code, error_message)
                i += 3
            else:
                i += 1
        return error_dict

    except requests.RequestException as e:
        print("Failed to retrieve the website. Please try again later.")
        print(f"RequestException: {e}")
        return {}

    except Exception as e:
        print("An error occurred:", e)
        return {}

if __name__ == '__main__':
    error_dict = fetch_error_codes()
    
    app = QApplication(sys.argv)
    ex = ErrorLookupApp(error_dict)
    ex.show()
    sys.exit(app.exec_())
