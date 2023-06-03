import json
import requests
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from datetime import datetime


class BtnClass:
    def __init__(self):
        """инициалиация класса"""
        self.headers = {"Content-Type": "application/json"}
        self.url = 'http://127.0.0.1:5000'
        self.count_post = 0

    def post_request(self, date):
        url = f'{self.url}/db/save'
        try:
            requests.post(url=url, data=date, headers=self.headers)
        except:
            return None

    def create_json(self, message):
        """Формирование json для отправки"""
        current_time = datetime.now()
        data = {'message': message,
                'date': str(current_time.date()),
                'tame': str(current_time.time()),
                'count': self.count_post}
        return json.dumps(data)

    def btn_post_logic(self, message):
        """Клики считаются всегда, а отправляются только не путые запросы"""
        self.count_post += 1
        if message:
            json_data = self.create_json(message)
            self.post_request(json_data)

    def get_request(self):
        url = f'{self.url}/db/resources'
        try:
            response = requests.get(url=url, headers=self.headers)
        except:
            return None
        return response.json()

    @staticmethod
    def query_result_output(json_data):
        model = QStandardItemModel()
        if json_data is None:
            model.appendRow(QStandardItem("Подключение к серверу не установлено"))
        elif json_data['data']:
            for data in json_data['data']:
                model.appendRow(QStandardItem(str(data)))
        else:
            model.appendRow(QStandardItem("Данных нет"))
        return model

    def btn_get_logic(self):
        json_data = self.get_request()
        return self.query_result_output(json_data)
