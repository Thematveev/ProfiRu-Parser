from driver import Driver
from notifier import TelegramNotifier
from time import sleep
from config_reader import get_telegram_credentials, get_timeout


TIMEOUT = get_timeout()
TOKEN, CHAT_ID = get_telegram_credentials()

tn = TelegramNotifier(TOKEN, CHAT_ID)
driver = Driver()


def main():
    driver.login()
    sent = []
    try:
        while True:
            for order in driver.parseOrders():
                if order['id'] not in sent:
                    sent.append(order['id'])
                    tn.sendMessage(str(order))
                    sleep(TIMEOUT * 60)
    except:
        tn.sendMessage("Server error!")
                




if __name__ == "__main__":
    main()