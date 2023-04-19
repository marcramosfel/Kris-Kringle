import secret_santa
import whatsapp_send_participants

def main():
    print("   _   _   _   _   _   _   _   _   _   _   _   _ ")
    print("  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ")
    print(" ( S | e | c | r | e | t |   | S | a | n | t | a )")
    print("  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  ")
    print(" ")
    while True:
        print(" ")
        print("       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("       +   Welcome to the greeting menu!   +")
        print("       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n       +                                   +")
        print("       +   1. Random by your input         +\n       +                                   +")
        print("       +   2. Random by a csv file         +\n       +                                   +")
        print("       +   3. Quit                         +")
        print("       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        choice = input("Enter your selection: ")

        if choice == "1":
            participants = secret_santa.participants_list_from_input()
            print('Shuffling participants ...')
            secret_santas_shuffled = secret_santa.shuffle_participants(participants)
            for person, secret_santa in secret_santas_shuffled.items():
                print(f'{person.name} will be the secret santa for {secret_santa.name}')
                print(person.__repr__)
                whatsapp_send_participants.send_whatsapp_message(person.name, )

        elif choice == "2":
            csv_file_name = input("Enter your csv file name: ")
            try:
                participants = secret_santa.participants_list_from_csv(csv_file_name)
                secret_santa.shuffle_participants(participants)
            except IOError:
                print('You may have selected the wrong file or writed it wrong. Try again!')

        elif choice == "3":
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()  # Output: "This is the main function"
