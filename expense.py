from PyInquirer import prompt
from csv import writer, reader

file_name = "expense_report.csv"

list_spender = []

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    # {
    #     "type":"input",
    #     "name":"spender",
    #     "message":"New Expense - Spender: ",
    # },
    {
        "type":"list",
        "name":"list_spender",
        "message":"Pick a spender:",
        "choices": list_spender
    },
]

def try_catch_int(input):
    try:
        value = int(input)
        return True
    except ValueError:
        print("A number was excepted ! - Insertion Failed.")
        return False

def try_catch_str(input):
    try:
        value = int(input)
        print("Not a number ! - Insertion Failed.")
        return False
    except ValueError:
        return True

def check_input(infos):
    for (key, value) in infos.items():
        if (key == "amount"):
            if (not try_catch_int(value)):
                return False
        elif (key == "label" or key == "spender"):
            if (not try_catch_str(value)):
                return False
    return True

def write_in_csv(infos):
    line = []
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Iterate over infos
        for (key, value) in infos.items():
            line.append(value)
        csv_writer.writerow(line)
    return True

def feed_list_spender():
    list_spender.clear()
    with open('users.csv','r') as users:
        csv_reader = reader(users)
        for row in csv_reader:
            list_spender.append(row[0])

def new_expense(*args):
    feed_list_spender()
    infos = prompt(expense_questions)
    if (not check_input(infos)):
        return False
    insertion = write_in_csv(infos)
    if (insertion == True):
        print("Expense Added !")
        return True
    print("Insertion failed !")
    return False