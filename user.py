from PyInquirer import prompt
from csv import writer, reader

file_name = "users.csv"

user_questions = [
    {
        "type":"input",
        "name":"fullname",
        "message":"New User - Full Name: ",
    },
]

def write_in_csv(infos):
    line = []
    existingLines = []
    # Read csv to check user already register
    with open(file_name,'r') as file_check:
        csv_reader = reader(file_check)
        for row in csv_reader:
            existingLines.append(row[0])
    # Append in csv user if not exists
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for (key, value) in infos.items():
            if (value in existingLines):
                return False
            line.append(value)
        csv_writer.writerow(line)
    return True

def add_user():
    infos = prompt(user_questions)
    insertion = write_in_csv(infos)
    if (insertion == True):
        print("Expense Added !")
        return True
    print("Insertion failed, user already exists !")
    return False