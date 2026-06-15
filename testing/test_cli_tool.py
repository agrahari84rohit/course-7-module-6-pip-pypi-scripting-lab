import io
from contextlib import redirect_stdout

import cli_tool


def reset_users():
    cli_tool.users.clear()


def test_add_task_creates_user_and_task():
    reset_users()
    output = io.StringIO()

    with redirect_stdout(output):
        exit_code = cli_tool.main(["add-task", "Alice", "Write unit tests"])

    assert exit_code == 0
    assert "Alice" in cli_tool.users
    assert cli_tool.users["Alice"].tasks[0].title == "Write unit tests"
    assert "Task 'Write unit tests' added" in output.getvalue()


def test_complete_task_marks_task_done():
    reset_users()
    cli_tool.users["Alice"] = cli_tool.User("Alice")
    cli_tool.users["Alice"].add_task(cli_tool.Task("Write unit tests"))

    output = io.StringIO()
    with redirect_stdout(output):
        exit_code = cli_tool.main(["complete-task", "Alice", "Write unit tests"])

    assert exit_code == 0
    assert cli_tool.users["Alice"].tasks[0].completed is True
    assert "completed" in output.getvalue()


def test_list_tasks_shows_all_entries():
    reset_users()
    cli_tool.users["Alice"] = cli_tool.User("Alice")
    cli_tool.users["Alice"].add_task(cli_tool.Task("Write unit tests"))

    output = io.StringIO()
    with redirect_stdout(output):
        exit_code = cli_tool.main(["list-tasks", "Alice"])

    assert exit_code == 0
    assert "Write unit tests" in output.getvalue()
