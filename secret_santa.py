import random
import csv

class Person:
    def __init__(self, name:str, number:str) -> None:
        self.name = name
        self.numeber = number
    def __repr__(self) -> str:
        return f"{self.nome}"

def participants_list_from_input():
    participants = []

    # Set a flag to indicate whether we should continue getting inputs
    getting_inputs = True

    while getting_inputs:
        # Get an input from the user
        participant_name = input('Enter a name: \n(Write done for stop)')
        # Check if the user wants to stop
        if participant_name == 'done':
            getting_inputs = False
        else:
            number = str(input('Enter a number: '))
            participant_number = "+351" + number
            # Add the input to the list
            participant = Person(participant_name.title(), participant_number)
            participants.append(participant)
    
    return participants

def participants_list_from_csv(csv_file):
    participants = []
    # Open the CSV file
    csv_file_complete = 'C:/Users/marco/Desktop/projects/kris-kringle/' + csv_file
    with open(csv_file_complete, 'r') as file:
        # Create a CSV reader
        reader = csv.DictReader(file)

        # Iterate over the rows of the CSV file
        for row in reader:
            # Print the values of the row
            print(row['name'], row['number'])
            participant = Person(row['name'].title(), ('+351' + row['number']))
            
            # Add the input to the dict
            participants.append(participant)
    return participants

def shuffle_participants(participants):
    # Shuffle the list of participants randomly
    random.shuffle(participants)

    # Assign each person a secret santa
    secret_santas = {}
    for i in range(len(participants)):
        secret_santas[participants[i]] = participants[(i + 1) % len(participants)]

    # Print out the secret santa assignments
    for person, secret_santa in secret_santas.items():
        print(f'{person.name} will be the secret santa for {secret_santa.name}')


