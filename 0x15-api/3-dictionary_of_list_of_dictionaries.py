#!/usr/bin/python3
"""Gather data from an API
"""
import json
from sys import argv
from urllib.request import *


if __name__ == '__main__':
    usrUrl = f"https://jsonplaceholder.typicode.com/users"
    userResponse = urlopen(usrUrl)

    if userResponse.status == 200:
        usersData = json.load(userResponse)
    else:
        print(
            f"Failed to fetch data from the api,\
            HTTP RESPONSE: {userResponse.status}"
        )
    todo_all = {}
    for user_id in usersData:
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_id['id'])
        toDoResponse = urlopen(url)
        if toDoResponse.status == 200:
            toDoData = json.load(toDoResponse)
        else:
            print(
                f"Failed to fetch data from the api,\
                HTTP RESPONSE: {toDoResponse.status}"
            )

        user_data = {f"{user_id['id']}": []}
        for task in toDoData:
            user_data[f"{user_id['id']}"].append({
                'username': user_id['username'],
                'completed': task['completed'],
                'task': task['title']
            })
        todo_all.update(user_data)
    with open('todo_all_employees.json', 'w') as userfile:
        json.dump(todo_all, userfile, indent=4)
