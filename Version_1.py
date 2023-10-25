import telebot
from telebot import types

# Initialize your bot
botTimeWeb = telebot.TeleBot('6024824352:AAGNGxtNLpbI0XtMxnd_Vjqke7puzajqq80')

# Define the states
SELECT_SUBJECT, USEFUL, ADD_INFO, ADD_FEEDBACK, CONTINUE, END = range(6)

# Define the user states
user_states = {}


# Define the command handler for /start
@botTimeWeb.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = SELECT_SUBJECT
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton("Физика")
    item2 = types.KeyboardButton("Информатика")
    item3 = types.KeyboardButton("Математика")
    markup.add(item1, item2, item3)
    botTimeWeb.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}!\n"
        "Я твой бот помощник по школе. Выбери интересующий предмет:",
        reply_markup=markup
    )


# Define the function for selecting the subject
@botTimeWeb.message_handler(func=lambda message: user_states.get(message.from_user.id) == SELECT_SUBJECT)
def select_subject(message):
    user_id = message.from_user.id
    user_states[user_id] = USEFUL
    user_subject = message.text
    user_states[user_id] = USEFUL

    # Respond based on the selected subject
    if user_subject == "Физика":
        botTimeWeb.send_message(
            message.chat.id,
            "Вот ссылка на курс по Физике: [Физика на Coursera](https://www.coursera.org/courses?query=%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0)"
        )
    elif user_subject == "Информатика":
        botTimeWeb.send_message(
            message.chat.id,
            "Вот ссылка на курс по Информатике: [Информатика на Coursera](https://www.coursera.org/courses?query=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)"
        )
    elif user_subject == "Математика":
        botTimeWeb.send_message(
            message.chat.id,
            "Вот ссылка на курс по Математике: [Математика на Coursera](https://www.coursera.org/courses?query=%D0%BC%D0%B0%D1%82%D0%B5%D0%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)"
        )

    user_states[user_id] = USEFUL
    botTimeWeb.send_message(message.chat.id, "Была ли полезна информация? (Да/Нет)")


# Define the function for handling the usefulness response
@botTimeWeb.message_handler(func=lambda message: user_states.get(message.from_user.id) == USEFUL)
def useful_info(message):
    user_id = message.from_user.id
    user_response = message.text.lower()

    if user_response == 'да':
        botTimeWeb.send_message(message.chat.id, "Вы хотели бы что-то добавить? (Да/Нет)")
        user_states[user_id] = ADD_INFO
    elif user_response == 'нет':
        markup = types.ReplyKeyboardRemove(selective=False)
        botTimeWeb.send_message(message.chat.id, "Спасибо, успехов в учебе!", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton("Начать сначала")
        item2 = types.KeyboardButton("Завершить сеанс")
        markup.add(item1, item2)
        botTimeWeb.send_message(message.chat.id, "Что бы вы хотели сделать?", reply_markup=markup)
        user_states[user_id] = END
    else:
        botTimeWeb.send_message(message.chat.id, "Пожалуйста, выберите 'Да' или 'Нет'. (Да/Нет)")


# Define the function for handling adding information
@botTimeWeb.message_handler(func=lambda message: user_states.get(message.from_user.id) == ADD_INFO)
def add_info(message):
    user_id = message.from_user.id
    user_response = message.text.lower()

    if user_response == 'да':
        botTimeWeb.send_message(message.chat.id,
                                "Что бы вы добавили, напишите пожалуйста, я стараюсь быть лучше, благодаря Вам!")
        user_states[user_id] = ADD_FEEDBACK
    elif user_response == 'нет':
        markup = types.ReplyKeyboardRemove(selective=False)
        botTimeWeb.send_message(message.chat.id, "Спасибо, успехов в учебе!", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton("Начать сначала")
        item2 = types.KeyboardButton("Завершить сеанс")
        markup.add(item1, item2)
        botTimeWeb.send_message(message.chat.id, "Что бы вы хотели сделать?", reply_markup=markup)
        user_states[user_id] = END
    else:
        botTimeWeb.send_message(message.chat.id, "Пожалуйста, выберите 'Да' или 'Нет'. (Да/Нет)")


# Define the function for handling feedback
@botTimeWeb.message_handler(func=lambda message: user_states.get(message.from_user.id) == ADD_FEEDBACK)
def add_feedback(message):
    user_id = message.from_user.id
    feedback = message.text
    botTimeWeb.send_message(message.chat.id,
                            "Спасибо, я учту ваши пожелания. Для продолжения нажмите на кнопку 'Продолжить'.")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton("Продолжить")
    markup.add(item1)
    botTimeWeb.send_message(message.chat.id, "Что бы вы хотели сделать?", reply_markup=markup)
    user_states[user_id] = CONTINUE


# Define the function to restart or end the conversation
@botTimeWeb.message_handler(func=lambda message: user_states.get(message.from_user.id) == CONTINUE)
def restart_or_end(message):
    user_id = message.from_user.id
    if message.text.lower() == "начать сначала":
        user_states[user_id] = SELECT_SUBJECT
        markup = types.ReplyKeyboardRemove(selective=False)
        botTimeWeb.send_message(message.chat.id, "Начнем сначала. Выбери интересующий предмет:", reply_markup=markup)
    elif message.text.lower() == "завершить сеанс":
        markup = types.ReplyKeyboardRemove(selective=False)
        botTimeWeb.send_message(message.chat.id, "Завершаю сеанс. Удачи в учебе!", reply_markup=markup)
        user_states[user_id] = None
    else:
        botTimeWeb.send_message(message.chat.id, "Пожалуйста, выберите 'Начать сначала' или 'Завершить сеанс'.")


# Run the bot
if __name__ == "__main__":
    botTimeWeb.polling()
