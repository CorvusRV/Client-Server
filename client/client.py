import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QListView, QLineEdit, QLabel, QGridLayout, QWidget
from btn_logic import BtnClass


class MainWindow(QWidget):
    def __init__(self):
        """инициализация объекта для создания окана приложения"""
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle('CLIENT')
        self.title_message = QLabel('Сообщение:', self)
        self.text_message = QLineEdit(self)
        self.btn_post = QPushButton('ОТПРАВИТЬ', self)
        self.btn_get = QPushButton('ПОЛУЧИТЬ', self)
        self.title_get = QLabel('Результат', self)
        self.text_get = QListView()
        self.create_form()
        self.add_functions()

    def create_form(self):
        """расположение элементов в окне приложения"""
        form = QGridLayout()
        form.addWidget(self.title_message, 1, 0)
        form.addWidget(self.text_message, 1, 1, 1, 3)
        form.addWidget(self.btn_post, 2, 0, 2, 2)
        form.addWidget(self.btn_get, 2, 2, 2, 2)
        form.addWidget(self.title_get, 3, 0)
        form.addWidget(self.text_get, 4, 0, 6, 4)
        self.setLayout(form)

    def add_functions(self):
        """запуск функци объектов"""
        self.btn_post.clicked.connect(self.btn_post_function)
        self.btn_get.clicked.connect(self.btn_get_function)

    def btn_post_function(self):
        """Логика кнопка "Отправить"""
        message = self.text_message.text()
        btn.btn_post_logic(message)

    def btn_get_function(self):
        """Логика кнопка "Получить"""
        model = btn.btn_get_logic()
        self.text_get.setModel(model)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
btn = BtnClass()
sys.exit(app.exec())
