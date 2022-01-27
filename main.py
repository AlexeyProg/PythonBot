import random
import telebot


HELP = "Справка по программе"
token = '5043459184:AAE0lzfY51HOZpI-sMImiFUTsyOJSxoQgd8'
bot = telebot.TeleBot(token)

def help(message):
    bot.send_message(message.chat.id, HELP)


bot.polling(none_stop=True)



RANDOM_TASK = ["Записаться","Гамзануть","Skam"]

tasks = {

}
run = True

def add_command(date,task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на ", date)


while run:
    command = input("Введите команду: ")
    if command == "help":
        print(help)

    elif command == "show":
        date = input("Введите дату для просмотра задач: ")
        if date in tasks:
            for task in tasks[date]:
                print("-", task)
        else:
            print("Такой даты нет")

    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        add_command(date,task)

    elif command == "random":
        task = random.choice(RANDOM_TASK)
        add_command("Сегодня",task)

    else:
        print("Команда неизвестна")
        run = False
        print("Программа завершена")
