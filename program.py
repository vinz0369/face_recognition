import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from subprocess import Popen

class ProgramLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Nhan dien guong mat')

        button1 = QPushButton('Luu khuon mat moi', self)
        button1.move(50, 50)
        button1.clicked.connect(self.run_program1)

        button2 = QPushButton('Quet khuon mat', self)
        button2.move(150, 50)
        button2.clicked.connect(self.run_program2)

    def run_program1(self):
        Popen(['python', 'face_dataset.py'])

    def run_program2(self):
        Popen(['python', 'face_recognition.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = ProgramLauncher()
    launcher.show()
    sys.exit(app.exec_())
