import json
import csv
from csv import DictReader

users_list = []
user_keys = ["name", "gender", "address", "age"]
book_keys = {"Title", "Author", "Pages", "Genre"}

with open("../files/users.json", "r") as f:
    users = json.loads(f.read())

for user in users:
    user_item = {k: user[k] for k in user_keys}
    user_item["books"] = []
    users_list.append(user_item)

# Initial iterator creation
users_iter = (user for user in users_list)

with open('../files/books.csv', newline='') as f:
    books = DictReader(f)

    for book in books:
        try:
            book_item = {k: book[k] for k in book_keys}
            next(users_iter)["books"].append(book)
        except StopIteration:
            # New iterator creation, new circle through users starts
            users_iter = (user for user in users_list)

# Write result to file

result_list = []

users_iter = (user for user in users_list)

while True:
    try:
        result_list.append(next(users_iter))
    except StopIteration:
        break


with open("../files/result.json", "w") as f:
    s = json.dumps(result_list, indent=4)
    f.write(s)
