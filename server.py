from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None

            print("------------------------------")
            chatID = item["message"]["chat"]["id"]
            messID = item["message"]["message_id"]
            print(chatID)
            print(messID)
            print(message)
            if message is not None:
                if "?" not in message and "https" not in message and "http" not in message and "www." not in message:
                   bot.deleteNotNeeded(message, messID ,chatID)
