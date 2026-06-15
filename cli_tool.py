"""Command-line task manager built with argparse and OOP classes."""

import argparse

from lib.models import Task, User


users = {}


def add_task(args):
    """Create the user if needed and add a task to their list."""
    user = users.get(args.user) or User(args.user)
    users[args.user] = user

    task = Task(args.title)
    user.add_task(task)
    return 0


def list_tasks(args):
    """Show all tasks for the named user."""
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return 1

    if not user.tasks:
        print(f"{user.name} has no tasks yet.")
        return 0

    print(f"{user.name}'s tasks:")
    for index, task in enumerate(user.list_tasks(), start=1):
        status = "completed" if task.completed else "pending"
        print(f"  {index}. {task.title} [{status}]")

    return 0


def complete_task(args):
    """Mark a named task complete for the selected user."""
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return 1

    for task in user.tasks:
        if task.title == args.title:
            task.complete()
            return 0

    print("❌ Task not found.")
    return 1


def build_parser():
    """Create the CLI parser and command definitions."""
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task", aliases=["add"], help="Add a task")
    add_parser.add_argument("user", help="Name of the user")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list-tasks", aliases=["list"], help="List tasks")
    list_parser.add_argument("user", help="Name of the user")
    list_parser.set_defaults(func=list_tasks)

    complete_parser = subparsers.add_parser(
        "complete-task", aliases=["complete"], help="Complete a task"
    )
    complete_parser.add_argument("user", help="Name of the user")
    complete_parser.add_argument("title", help="Title of the task to complete")
    complete_parser.set_defaults(func=complete_task)

    return parser


def main(argv=None):
    """Run the CLI using the provided argument list."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "func"):
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
