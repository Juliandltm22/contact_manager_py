# Functions for entire program

def print_list(contact_list):
    """
    Prints the contact list
    """
    print("================== CONTACT LIST ==================")
    print(f'{"Index":8}{"First Name":22}{"Last Name":22}')
    print("======  ====================  ====================")

    for i in range(len(contact_list)):
        print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')


def add_contact(contact_list):
    """
    Allows user to add to their contacts
    """
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ") 
    contact_list.append([first_name, last_name])
    return contact_list
    

def modify_contact(contact_list):
    """
    Allows user to modify their contact
    """
    index_num_mod = int(input("Enter the index number: "))
    if index_num_mod < 0 or index_num_mod >= len(contact_list):
        print("Invalid index number.")
        return contact_list
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    contact_list[index_num_mod] = [first_name, last_name]
    return contact_list     


def delete_contact(contact_list):
    """
    Allows the user to delete contacts
    """
    index_delete_num = int(input("Enter the index you woud like to delete: "))
    if index_delete_num < 0 or index_delete_num >= len(contact_list):
        print("Invalid index number")
        return contact_list
    del contact_list[index_delete_num]
    return contact_list
