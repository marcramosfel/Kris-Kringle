import random
import csv


class Person:
    def __init__(self, name: str, number: str) -> None:
        self._name = name
        self._number = '+351' + number
        self._code = self.generate_code()

    def __repr__(self) -> str:
        return f"{self.name}, has the number {self.number}, and received this code: {self.code} to authenticate."

    @property
    def get_name(self):
        return self._name

    @property
    def get_number(self):
        return self._number

    @property
    def get_code(self):
        return self._code

    @staticmethod
    def generate_code():
        code = ""
        for i in range(5):
            code += str(random.randint(0, 9))
        return code


def get_participants_list_from_input():
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
            participant_number = number
            # Add the input to the list
            participant = Person(participant_name.title(), participant_number)
            participants.append(participant)

    return participants


def get_participants_list_from_csv(csv_file):
    participants = []
    # Open the CSV file
    csv_file_complete = 'C:/Users/marcramos/Desktop/projects/kris-kringle/' + csv_file
    with open(csv_file_complete, 'r') as file:
        # Create a CSV reader
        reader = csv.DictReader(file)

        # Iterate over the rows of the CSV file
        for row in reader:
            # Print the values of the row
            print(row['name'], row['number'])
            participant = Person(row['name'].title(), (row['number']))

            # Add the input to the dict
            participants.append(participant)
    return participants


def get_shuffle_participants(participants):
    # Shuffle the list of participants randomly
    random.shuffle(participants)

    # Assign each person a secret santa
    secret_santas = {}
    for i in range(len(participants)):
        secret_santas[participants[i]] = participants[(i + 1) % len(participants)]

    # Print out the secret santa assignments
    for person, secret_santa in secret_santas.items():
        print(type(person.get_name))
        #print(f'{person.get_name()} will be the secret santa for {secret_santa.get_name()} and the code is {person.get_code()}.')
        #print(person.__repr__)

    return secret_santas
