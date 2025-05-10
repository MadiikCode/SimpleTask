import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_NAME = "todos.txt"

def load_todos():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("")
    with open(FILE_NAME, "r") as file:
        todos = []
        for line in file.readlines():
            line = line.strip()
            if line:
                if " | " not in line:
                    line = f"{line} | {datetime.now().strftime('%Y-%m-%d')}"
                todos.append(line)
    return todos

def save_todos(todos):
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(todos))

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("400x400")
        self.todos = load_todos()

        # Стиль
        self.root.configure(bg="#f0f0f0")
        self.font = ("Arial", 12)

        # Виджеты
        self.label = tk.Label(root, text="Мои задачи:", bg="#f0f0f0", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, width=50, height=15, font=self.font, selectbackground="#a6a6a6")
        self.listbox.pack(pady=5)
        self.update_listbox()

        self.add_button = tk.Button(root, text="➕ Добавить", command=self.add_task, bg="#4CAF50", fg="white", font=self.font)
        self.add_button.pack(pady=5, fill=tk.X, padx=20)

        self.delete_button = tk.Button(root, text="❌ Удалить", command=self.delete_task, bg="#f44336", fg="white", font=self.font)
        self.delete_button.pack(pady=5, fill=tk.X, padx=20)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.todos:
            if " | " in task:
                task_text, task_date = task.split(" | ")
                self.listbox.insert(tk.END, f"{task_text} ({task_date})")
            else:
                self.listbox.insert(tk.END, task)

    def add_task(self):
        task_text = simpledialog.askstring("Добавить задачу", "Введите задачу:")
        if task_text:
            task_date = datetime.now().strftime("%Y-%m-%d")
            self.todos.append(f"{task_text} | {task_date}")
            save_todos(self.todos)
            self.update_listbox()
            messagebox.showinfo("Успех", "Задача добавлена!")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            deleted_task = self.todos.pop(selected_index)
            save_todos(self.todos)
            self.update_listbox()
            messagebox.showinfo("Удалено", f"Задача '{deleted_task.split(' | ')[0]}' удалена!")
        except IndexError:
            messagebox.showerror("Ошибка", "Выберите задачу для удаления!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()