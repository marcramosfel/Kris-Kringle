import secret_santa
def main():
    print("   _   _   _   _   _   _   _   _   _   _   _   _ ")
    print("  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ")
    print(" ( S | e | c | r | e | t |   | S | a | n | t | a )")
    print("  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  ")
    print("")
    while True:
        print("Welcome to the greeting menu!")
        print("1. Random by your input")
        print("2. Random by a csv file")
        print("3. Quit")

        choice = input("Enter your selection: ")

        if choice == "1":
            participants = secret_santa.participants_list_from_input()
            secret_santa.suffle_participants(participants)
        elif choice == "2":
            csv_file_name = input("Enter your csv file name: ")
            participants = secret_santa.participants_list_from_csv(csv_file_name)
            secret_santa.suffle_participants(participants)
        elif choice == "3":
            break
        else:
            print("Invalid selection. Please try again.")



if __name__ == "__main__":
  main()  # Output: "This is the main function"