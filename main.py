import contacts

list = []
while True: 
    print("\n*** MAIN MENU ***")
    print("1. Print list")
    print("2. Add Contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Exit the program")

    menu_choice = input("\nEnter your menu choice: ")

    if menu_choice == '1':
        contacts.print_list(list)
    elif menu_choice == '2':
        list = contacts.add_contact(list)
    elif menu_choice == '3':
        list = contacts.modify_contact(list)
    elif menu_choice == '4':
        list = contacts.delete_contact(list)
    elif menu_choice == '5':
        break
