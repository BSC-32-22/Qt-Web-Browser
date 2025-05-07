import sys
import time 
#from pathlib import Path
from PyQt5.QtWidgets import QApplication,QMessageBox, QMainWindow, QVBoxLayout,QHBoxLayout, QWidget, QLineEdit,QPushButton,QToolButton
from PyQt5.QtCore import QUrl 

from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UNIMA Browser")
        self.setWindowIcon(QIcon(QPixmap('/Icons_Logos/UNIMA_Logo.png')))
        self.setGeometry(100, 100, 1200, 800)

        #browser screen
        self.browser = QWebEngineView()

        #search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('🔍 Search the web')
        self.search_bar.setStyleSheet("QLineEdit{border: 1px solid blue;}")
        self.search_bar.returnPressed.connect(self.search)
        
        #navigation buttons
        #back_button
        self.back_button = QPushButton()
        self.back_button.setIcon(QIcon('Icons_Logos/back.svg'))
        self.back_button.setStyleSheet("background-color: blue;")
        self.back_button.clicked.connect(self.browser.back)
        #forward_button
        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon('Icons_Logos/forward.svg'))
        self.forward_button.setStyleSheet("background-color: blue;")
        self.forward_button.clicked.connect(self.browser.forward)
        #reload button
        self.reload_button = QPushButton()
        self.reload_button.setIcon(QIcon('Icons_Logos/reload.svg'))
        self.reload_button.setStyleSheet("background-color: blue;")
        self.reload_button.clicked.connect(self.browser.reload)
        #home button
        self.home_button = QPushButton()
        self.home_button.setIcon(QIcon('Icons_Logos/home.svg'))
        self.home_button.setStyleSheet("background-color: blue;")
        self.home_button.clicked.connect(lambda: self.browser.setUrl(QUrl.fromLocalFile("/pages/Welcome_Page.html"))) 
        

        #layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout_1 = QHBoxLayout()
        layout_1.addWidget(self.back_button)
        layout_1.addWidget(self.forward_button)
        layout_1.addWidget(self.reload_button)
        layout_1.addWidget(self.home_button)
        layout_1.addWidget(self.search_bar)
        layout.addLayout(layout_1)
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        
        #set homePage
        self.browser.setUrl(QUrl.fromLocalFile("/pages/Welcome_Page.html"))
        

    def search(self):
        url = self.search_bar.text().strip().lower()
        #local server url
        local_server_url = 'http://localhost:8085/'
 
        #check input and add needful extensions
        if not url:
            return
        #local search check 
        elif url in ("index","register"):
            if url == 'index':
                url = local_server_url
            else: 
                url = f"{local_server_url}register"
        else:
             not_found_page = f"""<!DOCTYPE html> 
                                    <html> 
                                    <head> 
                                        <title>Not Found</title> 
                                    </head>
                                    <body style="text-align: center;">
                                        <h2>No results found for ‘{url}’. Try searching on Google?</h2>
                                        <form method="get" action="https://www.google.com/search" style="margin-top: 10px;">
                                            <input type="hidden" name="q" value="{url}">
                                            <input type="submit" value="Search using Google">
                                        </form> 
                                    </body>
                                    </html>"""
             #set Html as per query given
             self.browser.setHtml(not_found_page)
             return
        #search web 
        self.browser.setUrl(QUrl(url))
        
        
     
            
    
app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
