import requests

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat = chat_id

    def sendMessage(self, text):
        link = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat}&text={text}'
        requests.get(link)