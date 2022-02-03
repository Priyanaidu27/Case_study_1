
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response)
todos = json.loads(response.text)

print("Total Completed Todos are",sum(1 for todo in todos if todo['completed']))

###Total Completed Todos are 90