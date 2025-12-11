''' This will be a simple contact managemet system that has the following functionalities:

1.  Add a new contact (with name, phone number and email)
2.  Search for a contact by name
3.  Update a contact's information
4.  Delete a contact '''

print('''Contact Management System\n
There are a variety of options to choose from, input the letter for each function you wish to perform:\n
a. Add a new contact (with name, phone number and email)\n
b. Search for a contact by name\n
c. Update a contact's information\n
d. Delete a contact\n
''')

def add_contact(contacts: dict) -> dict: 

    '''In this function we will perform the actions for adding a contact!
       Args: contacts dictionary (stores all contacts)'''

    name = input('What is the name of the contact you wish to add? ').lower() #lowercase it to avoid issues 

    phone = input('What is the phone number? ')

    clean_number = phone.replace('-', '') #if an user inputs the number as 123-444 it'll store it as 123444

    email = input('Enter an email: ').lower()

    if any(num.isalpha() for num in clean_number): #Loop through the phone number to make sure every value is numerical using isalpha()

        print("Enter a valid phone number!")

        return contacts # Keep validation and return contacts after invalid input so we don’t continue with bad data.

    if '@' not in email:

        print('Enter a valid email address please.')

        return contacts

    if name in contacts:

        print('This contact already exists!')

        return contacts

    # Add the contact
    contacts[name] = {

        "phone": clean_number,

        "email": email
    }

    print(f'Your contact {name}, with phone number {clean_number}, and email {email} has been successfully added!')

    return contacts 


def search_contact(contacts: dict) -> dict:

    '''This function will search for the specified contact'''

    name = input('Enter the name to search: ')

    if name not in contacts:

        print('Contact not found!\n')

        return contacts

    contact = contacts[name]

    print(f'''Contact information found:\n
          
        Name: {name}

        Phone Number: {contact["phone"]}

        Email: {contact["email"]}\n''')

    return contacts 


def update_contact(contacts: dict) -> dict: 

    '''This function will update the specified contact'''

    name = input('What is the name of the contact you wish to update? ')

    if name not in contacts:

        print("Contact not found!")

        return contacts

    updated_name = input('What will be the new name? (Press Enter to keep current) ')

    updated_phone = input('What is the new phone number? (Press Enter to keep current) ')

    updated_email = input('What is the new email? (Press Enter to keep current) ').lower()

    contact = contacts[name]

    if updated_name == "":

        updated_name = name  #if user doesn't have any input, return original value 

    if updated_phone != "": #an input never returns Null so "" is the correct way to check for null values.

        updated_phone = updated_phone.replace('-', '')

        if any(num.isalpha() for num in updated_phone):

            print("Invalid phone number.")

            return contacts
    else:

        updated_phone = contact["phone"]

    if updated_email != "":

        if '@' not in updated_email:

            print("Invalid email.")

            return contacts
    else:

        updated_email = contact["email"]

    del contacts[name]  # remove old key

    contacts[updated_name] = {

        "phone": updated_phone,

        "email": updated_email
    }

    print(f'''Contact information updated:\n
          
Name: {updated_name}

Phone Number: {updated_phone}

Email: {updated_email}\n''')

    return contacts
            

def delete_contact(contacts: dict) -> dict:

    '''This function will delete the specified contact'''

    name = input('What is the name of the contact you wish to delete? ')

    if name in contacts:

        del contacts[name]

        print("Contact deleted!")

    else:

        print("Contact not found!")

    return contacts 


# CONTACT LIST (dictionary of contact dictionaries)

contacts = {}

while True:

    try:

        user_input = input('Choose an option: ').lower()

        match user_input:

            case 'a':

                add_contact(contacts)

            case 'b':

                search_contact(contacts)

            case 'c':

                update_contact(contacts)

            case 'd':

                delete_contact(contacts)

            case _:

                print("Invalid option.")

    except ValueError as e:

        print(f"An error occurred: {e}. Make sure you're typing the right data!")

    except Exception as e:

        print(f"An unexpected error occurred: {e}.")
