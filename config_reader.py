import json

def get_credentials():
    try:
        with open("config.json", 'r', encoding='UTF-8') as config:
            data = json.loads(config.read())
            return data['user'], data['password']
    except:
        print("No credentials: Please configure app in config.json")
        quit()

def get_telegram_credentials():
    try:
        with open("config.json", 'r', encoding='UTF-8') as config:
            data = json.loads(config.read())
            return data['telegramTOKEN'], data['chat_id']
    except:
        print("No credentials: Please configure app in config.json")
        quit()

def get_timeout():
    try:
        with open("config.json", 'r', encoding='UTF-8') as config:
            data = json.loads(config.read())
            return data['timeout_min']
    except:
        print("No credentials: Please configure app in config.json")
        quit()

if __name__ == "__main__":
    print(get_credentials())
    print(get_telegram_credentials())
    print(get_timeout())
        