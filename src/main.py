import json
import csv
from csv import DictReader

with open("../files/users.json", "r") as f:
    users = json.loads(f.read())

users_list = []

for user in users:
    user_item = {"name": user["name"], "gender": user["gender"], "address": user["address"], "age": user["age"], "books": [] }
    users_list.append(user_item)

# Initial iterator creation
users_iter = (user for user in users_list)

with open('../files/books.csv', newline='') as f:
    books = DictReader(f)

    for book in books:
        try:
            book_item = {"Title": book["Title"], "Author": book["Author"], "Pages": book["Pages"], "Genre": book["Genre"]}
            next(users_iter)["books"].append(book)
        except StopIteration:
            # New iterator creation, new circle through users starts
            users_iter = (user for user in users_list)


result_list = []
to_run = True
while to_run:
    try:
        result_list.append(next(users_iter))
    except StopIteration:
        to_run = False


with open("../files/result.json", "w") as f:
    s = json.dumps(result_list, indent=4)
    f.write(s)