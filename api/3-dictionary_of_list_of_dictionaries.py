#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests


def all_employee_todo_lists():
    """This function exports todo list data to json"""

    site_url = "https://jsonplaceholder.typicode.com"
    employees_url = f"{site_url}/users"
    todos_url = f"{site_url}/todos"

    employees = requests.get(employees_url).json()

    all_todo_lists = {}
    for employee in employees:
        employee_id = employee['id']
        username = employee['username']

        response = requests.get(todos_url, params={"userId": employee_id})
        todo_list = response.json()

        data = [{
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        } for todo in todo_list]

        all_todo_lists[str(employee_id)] = data

    file = "todo_all_employees.json"
    try:
        with open(file, 'w') as f:
            json.dump(all_todo_lists, f)
    except FileNotFoundError:
        print("The todo_all_employees file doesn't exist")


if __name__ == "__main__":
    all_employee_todo_lists()
