from PyInquirer import prompt
from csv import writer, reader

list_expense = []
list_contributor = []
list_users = []

refund_questions = [
    {
        "type":"list",
        "name":"list_expense",
        "message":"Pick an expense:",
        "choices": list_expense
    },
    {
        'type': 'checkbox',
        'qmark': 'X',
        'message': 'Select contributors',
        'name': 'contributors',
        'choices': list_users
    },
]

amount_question = [
    {
        "type":"list",
        "name":"list_contributors",
        "message":"Pick a contributor:",
        "choices": list_contributor
    },
    {
        "type":"input",
        "name":"amount",
        "message":"New Refund - Amount: ",
    },
]

def feed_list_user():
    list_users.clear()
    with open('users.csv','r') as users:
        csv_reader = reader(users)
        for row in csv_reader:
            list_users.append({"name": row[0]})

def feed_list_expenses():
    list_expense.clear()
    with open('expense_report.csv','r') as expenses:
        csv_reader = reader(expenses)
        for row in csv_reader:
            list_expense.append({"name": " ".join(row)})

def write_refund(infos_refund):
    return toto

def new_refund(*args):
    feed_list_expenses()
    feed_list_user()
    infos = prompt(refund_questions)
    for (key, value) in infos.items():
        print("this is the keys", key, value)
        if (key == 'contributors'):
            for user in value:
                infos_refund = prompt(amount_question)
                print(infos_refund)
    return False
