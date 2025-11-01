

import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt 

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Calculator")
        self.setFixedSize(300, 400) 
        main_layout = QVBoxLayout()
        self.display = QLineEdit() 
        self.display.setReadOnly(True) 
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  
        self.display.setFixedHeight(50)  
        self.display.setStyleSheet("font-size: 20px;") 

        
        main_layout.addWidget(self.display)

        button_layout = QGridLayout()

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
            'C': (4, 0), '←': (4, 1)
        }

  
        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text) 
            button.setFixedSize(60, 60) 
            button.setStyleSheet("font-size: 18px;") 
            button_layout.addWidget(button, pos[0], pos[1]) 
            button.clicked.connect(self.on_button_click) 


        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

   
    def on_button_click(self):
        button = self.sender()  
        text = button.text()  

    
        if text == "C":
            self.display.setText("")

       
        elif text == "←":
            self.display.setText(self.display.text()[:-1])

       
        elif text == "=":
            try:
                result = str(eval(self.display.text()))  
                self.display.setText(result)  
            except Exception:
                self.display.setText("Error")  

       
        else:
            self.display.setText(self.display.text() + text)


    def keyPressEvent(self, event):
        key = event.key()  

   
        if Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
            self.display.setText(self.display.text() + event.text())

        elif key in (Qt.Key.Key_Plus, Qt.Key.Key_Minus, Qt.Key.Key_Asterisk, Qt.Key.Key_Slash):
            self.display.setText(self.display.text() + event.text())


        elif key == Qt.Key.Key_Period:
            self.display.setText(self.display.text() + ".")

        elif key in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")


        elif key == Qt.Key.Key_Backspace:
            self.display.setText(self.display.text()[:-1])

        elif key == Qt.Key.Key_Escape:
            self.display.setText("")


        else:
            super().keyPressEvent(event)


if __name__ == "__main__"
    app = QApplication(sys.argv)
    window = Calculator()         
    window.show()                 
    sys.exit(app.exec())         
