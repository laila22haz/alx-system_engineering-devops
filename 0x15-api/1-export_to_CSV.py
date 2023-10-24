#!/usr/bin/python3
"""Gather data from an API
"""
import requests
import sys
import json
import csv


def gather_data(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    employee_info = response.json()
    username = employee_info['username']
    response = requests.get(f"{url}/todos")
    todo_list = response.json()

    with open(f'{id}.csv', 'w') as csvfile:
        for todo in todo_list:
            data = (f'"{id}", "{username}","{todo.get("completed")}",')
            data_ = (f'"{todo.get("title")}"\n')
            csvfile.write(data+data_)


if __name__ == "__main__":
    gather_data(sys.argv[1])
