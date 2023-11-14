import tkinter as tk
from tkinter import simpledialog
from todolist import ToDoList


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.view_button = tk.Button(self.master, text="View Tasks", command=self.view_tasks)
        self.edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.mark_completed_button = tk.Button(self.master, text="Mark Completed", command=self.mark_completed)
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)

        self.add_button.pack(side=tk.LEFT, padx=5)
        self.view_button.pack(side=tk.LEFT, padx=5)
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.mark_completed_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.exit_button.pack(side=tk.RIGHT, padx=5)

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            self.todo_list.add_task(description)
            self.update_listbox()

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.todo_list.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            self.task_listbox.insert(tk.END, f"{i}. {task.description} - {status}")

    def edit_task(self):
        task_index = self.get_selected_task_index()
        if task_index is not None:
            new_description = simpledialog.askstring("Edit Task", "Enter new task description:")
            if new_description:
                self.todo_list.edit_task(task_index, new_description)
                self.update_listbox()

    def mark_completed(self):
        task_index = self.get_selected_task_index()
        if task_index is not None:
            self.todo_list.mark_task_completed(task_index)
            self.update_listbox()

    def delete_task(self):
        task_index = self.get_selected_task_index()
        if task_index is not None:
            self.todo_list.delete_task(task_index)
            self.update_listbox()

    def get_selected_task_index(self):
        selection = self.task_listbox.curselection()
        if selection:
            return int(selection[0])
        return None

    def update_listbox(self):
        self.view_tasks()


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
