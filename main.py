"TASK netology.ru"
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи и выйти из программы."""

today = []
tomorrow = []
other = []

run = True
while run:

  command = input("Введите команду: ")
  if command == "exit":
    run = False
    print("Спасибо за использование! До свидания!")
  elif command == "HELP":
    print(HELP)
  elif command == "show":
    print("today", today)
    print("tomorrow", tomorrow)
    print("other", other)
    break
  elif command == "add":
    command = input("Когда выполнить задачу? -")
    if command == "сегодня":
      today.append(command)
    elif command == "завтра":
      tomorrow.append(command)
    else:
      other.append(command)
  else:
    print("Неизвестная команда. Для справки: HELP, выход из ПО: exit")
