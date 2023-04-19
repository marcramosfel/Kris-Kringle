import secret_santa
import create_pdf_file as cpf
from TwilioVersion import whatsapp_send_participant

file_path = ("C:\\Users\\marcramos\\Desktop\\projects\\Kris-Kringle\\pdf_files")


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
            participants = secret_santa.get_participants_list_from_csv()
            print('Shuffling participants ...\n')
            secret_santas_shuffled = secret_santa.get_shuffle_participants(participants)
            for person, secret_santa_var in secret_santas_shuffled.items():
                print(f'{person.name} will be the secret santa for {secret_santa_var.name}')
                # print(person.__repr__)
                # whatsapp_send_participants.send_whatsapp_message(person.name, )

        elif choice == "2":
            csv_file_name = input("Enter your csv file name: ")
            try:

                participants = secret_santa.get_participants_list_from_csv(csv_file_name)
                secret_santas_shuffled = secret_santa.get_shuffle_participants(participants)

                for person, secret_santa_var in secret_santas_shuffled.items():
                    message = f'Hello {person.get_name}, you will be the secret santa for: ** {secret_santa_var.get_name} **. Merry Christmas!'
                    cpf.create_protected_pdf(f"{file_path}\\Happy_Christmas_{person.get_name}.pdf", message, person.get_code, f"{file_path}\\Happy_Christmas_{person.get_code}.pdf")
                    print(f"Happy_Christmas_{person.get_name}", message, person.get_code)

                for person, secret_santa_var in secret_santas_shuffled.items():
                    print(file_path + f"\\Happy_Christmas_{person.get_name}.pdf")
                    whatsapp_send_participant.send_pdf_via_twilio(person.get_number, file_path + f"\\Happy_Christmas_{person.get_name}.pdf")
                    whatsapp_send_participant.send_sms_message(person.get_number, f"Your code for open the pdf file sent to your whatsapp is {person.get_code}")

            except IOError:
                print('You may have selected the wrong file or writed it wrong. Try again!')

        elif choice == "3":
            break

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()  # Output: "This is the main function"
