#!/usr/bin/python3
"""This script gathers data from an API for a given employee ID
    returns information about his/her TODO list progress"""

if __name__ == "__main__":
    import requests
    import sys
    import csv
    num = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    response = requests.get(api_url)
    name = response.json()["username"]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    response = requests.get(api_url)
    dicti = response.json()
    titles = []
    tasks = 0
    f = open('{}.csv'.format(num), 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for todo in dicti:
        row = [num]
        row.append(name)
        row.append(todo["completed"])
        row.append(todo["title"])
        writer.writerow(row)
    f.close()
