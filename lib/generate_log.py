"""Automation helper for the pip/PyPI scripting lab."""

from datetime import datetime

import requests


DEFAULT_LOG_DATA = [
    "User logged in",
    "User updated profile",
    "Report exported",
]


def generate_log(data):
    """Write a daily log file and return its filename."""
    if not isinstance(data, list):
        raise ValueError("data must be a list of log entries")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    return filename


def fetch_post_data():
    """Fetch a sample post from jsonplaceholder using requests."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"Warning: unable to fetch API data: {exc}")
        return {}


def main():
    """Run the automation tool from the command line."""
    filename = generate_log(DEFAULT_LOG_DATA)
    post = fetch_post_data()

    print(f"Log written to {filename}")
    print("Fetched Post Title:", post.get("title", "No title found"))


if __name__ == "__main__":
    main()
