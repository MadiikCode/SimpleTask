import os
from datetime import datetime
from colorama import init, Fore, Back, Style

# Инициализация colorama (для цветов в консоли)
init(autoreset=True)

FILE_NAME = "todos.txt"


# Загрузка задач из файла
def load_todos():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("")
    with open(FILE_NAME, "r") as file:
        todos = [line.strip() for line in file.readlines() if line.strip()]
    return todos


# Сохранение задач в файл
def save_todos(todos):
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(todos))


# Главное меню
def main():
    todos = load_todos()

    print(Fore.CYAN + "\n📝" + Fore.YELLOW + " To-Do List Manager " + Fore.CYAN + "📝")
    print(Fore.GREEN + "==========================")

    while True:
        print(Fore.WHITE + "\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input(Fore.BLUE + "Выберите действие (1-4): " + Style.RESET_ALL)

        if choice == "1":
            print(Fore.MAGENTA + "\n📋 Список задач:")
            if not todos:
                print(Fore.RED + "Нет задач!")
            else:
                for i, task in enumerate(todos, 1):
                    task_text, task_date = task.split(" | ")
                    print(f"{Fore.YELLOW}{i}. {task_text} {Fore.GREEN}({task_date})")

        elif choice == "2":
            task_text = input(Fore.BLUE + "Введите новую задачу: " + Style.RESET_ALL)
            task_date = datetime.now().strftime("%Y-%m-%d")
            todos.append(f"{task_text} | {task_date}")
            save_todos(todos)
            print(Fore.GREEN + "✅ Задача добавлена!")

        elif choice == "3":
            if not todos:
                print(Fore.RED + "Нет задач для удаления!")
            else:
                print(Fore.MAGENTA + "\n📋 Список задач:")
                for i, task in enumerate(todos, 1):
                    task_text, task_date = task.split(" | ")
                    print(f"{Fore.YELLOW}{i}. {task_text} {Fore.GREEN}({task_date})")
                try:
                    task_num = int(input(Fore.BLUE + "Номер задачи для удаления: " + Style.RESET_ALL)) - 1
                    if 0 <= task_num < len(todos):
                        deleted_task = todos.pop(task_num)
                        save_todos(todos)
                        print(Fore.RED + f"❌ Задача '{deleted_task.split(' | ')[0]}' удалена!")
                    else:
                        print(Fore.RED + "⚠ Неверный номер!")
                except ValueError:
                    print(Fore.RED + "⚠ Введите число!")

        elif choice == "4":
            print(Fore.CYAN + "Выход...")
            break

        else:
            print(Fore.RED + "⚠ Неверный выбор!")


if __name__ == "__main__":
    main()