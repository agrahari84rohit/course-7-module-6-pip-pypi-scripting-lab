"""Simple model classes for the task manager CLI."""


class Task:
    """Represent a single task that can be marked complete."""

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        self.title = title.strip()
        self.completed = False

    def complete(self):
        """Mark the task as complete and report the result."""
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    """Represent a user who can manage a list of tasks."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("User name cannot be empty.")

        self.name = name.strip()
        self.tasks = []

    def add_task(self, task):
        """Add a task to the user's list and confirm the action."""
        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task")

        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def list_tasks(self):
        """Return the user's task list."""
        return list(self.tasks)
