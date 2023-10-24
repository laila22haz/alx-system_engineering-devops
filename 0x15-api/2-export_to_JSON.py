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

    with open(f'{id}.json', 'w') as jsonfile:
        for todo in todo_list:
            data = {
                id: [
                    {
                        "task": todo.get("title"),
                        "completed": todo.get("completed"),
                        "username": username,
                        }
                    ]
            }
            json.dump(data, jsonfile)


if __name__ == "__main__":
    gather_data(sys.argv[1])
