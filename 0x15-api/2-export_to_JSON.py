#!/usr/bin/python3
"""Gather data from an API
"""
import json
import requests
import sys


def gather_data(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    employee_info = response.json()
    username = employee_info['username']
    response = requests.get(f"{url}/todos")
    todo_list = response.json()

    with open(f"{id}.json", "w") as f:
        data = {
            id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
                for task in todo_list
            ]
        }
        json.dump(data, f)


if __name__ == "__main__":
    gather_data(sys.argv[1])
