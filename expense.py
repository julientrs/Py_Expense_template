from PyInquirer import prompt
from csv import writer

file_name = "expense_report.csv"

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
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
]

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

def new_expense(*args):
    infos = prompt(expense_questions)
    insertion = write_in_csv(infos)
    if (insertion == True):
        print("Expense Added !")
        return True
    print("Insertion failed !")
    return False


