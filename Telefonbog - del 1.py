from multiprocessing.resource_sharer import stop


phonebook = {}

def show_phonebook():
    """Print all contacts in the phonebook."""
    for (name, phonenumber) in phonebook.items():
        print(name, ':', phonenumber)

def menu():
    """Display a menu, and ask the user to choose an option.
    Ensures that the chosen option is valid."""
    while True:
        print()
        print("0: quit")
        print("1: Print all contacts")
        print("2: Add contact")
        print("3: Remove contact")
        print("4: Look up contact by name")
        print()

        inp = input("> ")
        if inp.isdigit():
            i = int(inp)
            if i >= 0 and i <= 4:
                return i
        
        print("INVALID INPUT")

def main():
    """Main loop, where the menu is shown, the user chooses an option,
    and the relevant code is run."""
    while True:
        i = menu()
        
        if i == 0:
            break
        elif i == 1:
            show_phonebook()
        elif i == 2:
<<<<<<< Updated upstream
            name = input ('add name: ')
            while name in phonebook: 
=======
    # her tilføjes kode for at tilføje en ny kontakt
            name = input ('add name: ') 
            if name in phonebook: 
>>>>>>> Stashed changes
                print("this name does already exist")
                name = input ('add New name: ')
            phonenumber = input ('add new number: ')
            phonebook[name] = phonenumber
<<<<<<< Updated upstream
            print("Contact has been added to your phonebook")
=======
       
            else:
                print("Contact has been added to your phonebook")
            
>>>>>>> Stashed changes
        elif i == 3:
            name = input('type contact name you wish to delete: ')
            if name in phonebook:
                 del phonebook[name]
                 print ("Contact has been deleted")
            else: 
                print("Try again")
        elif i == 4:
<<<<<<< Updated upstream
            name = input ('search name: ')
            result= dict((phone_val,phone_k) for phone_val,phone_k in phonebook.items()).get(name)
            print(name, 'phonenumber is:',result)
=======
            # her tilføjes kode for at slå en kontakt op ved navn
            name = input ('search name: ')
            result= dict((phone_val,phone_k) for phone_val,phone_k in phonebook.items()).get('name')
        
            print("Dictionary search by value:",result)

>>>>>>> Stashed changes
if __name__ == "__main__":
    main()