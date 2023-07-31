while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

    user_input = input("Select an option (1, 2, or 3): ")

    if user_input == '3':
        print("Existing the program.")
        break

    if user_input == '1':
        print("You selected Option 1. ")

    elif user_input == '2':
        print("You selected Option 2.")

    else:
        print("Invalid option. Please choose a valid option (1, 2, or 3). ")

