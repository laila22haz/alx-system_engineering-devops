#!/usr/bin/python3
"""Gather data from an API
"""
import requests
import sys


def gather_data(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    employee_info = response.json()
    empl_name = employee_info['name']
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}/todos")
    todo_list = response.json()
    total = len(todo_list)
    completed = 0
    for task in todo_list:
        if task['completed'] is True:
            completed += 1
    print(f"Employee {empl_name} is done with tasks({completed}/{total}):")
    for task in todo_list:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    gather_data(sys.argv[1])
