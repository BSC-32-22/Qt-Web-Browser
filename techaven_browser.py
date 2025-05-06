import sys
#from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QHBoxLayout, QWidget, QLineEdit,QPushButton,QToolButton
from PyQt5.QtCore import QUrl 
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Techaven Browser")
        self.setWindowIcon(QIcon(QPixmap('MIT.jpg')))
        self.setGeometry(100, 100, 1200, 800)

        #browser screen
        self.browser = QWebEngineView()

        #search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('🔍 Search the web')
        self.search_bar.returnPressed.connect(self.search_web)
        
        #navigation buttons
        #back_button
        self.back_button = QPushButton()
        self.back_button.setIcon(QIcon('back_button.svg'))
        self.back_button.clicked.connect(self.browser.back)
        #reload button
        self.reload_button = QPushButton()
        # self.reload_button.setIcon(QIcon())
        self.reload_button.clicked.connect(self.browser.reload) 
        

        #layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout_1 = QHBoxLayout()
        layout_1.addWidget(self.back_button)
        layout_1.addWidget(self.reload_button)
        layout_1.addWidget(self.search_bar)
        layout.addLayout(layout_1)
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def search_web(self):
        url = self.search_bar.text()
        #check input
        if not url:
            return
        elif not url.startswith('https://'):
            url = 'https://' + url
        #search web 
        self.browser.setUrl(QUrl(url))
    
app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
