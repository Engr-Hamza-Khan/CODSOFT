from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.description} - {status}")

    def edit_task(self, task_index, new_description):
        self.tasks[task_index].edit_description(new_description)

    def mark_task_completed(self, task_index):
        self.tasks[task_index].mark_as_completed()

    def delete_task(self, task_index):
        del self.tasks[task_index]
