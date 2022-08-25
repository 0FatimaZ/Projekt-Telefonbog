from multiprocessing.resource_sharer import stop


phonebook = {}

class Contact:
    def __init__(self,
                 phonenumber,
                 email,
                 bd):
        self.phonenumber = phonenumber
        self.email = email
        self.bd = bd
    
    def bring(self):
        print("Tlf: " + str(self.phonenumber))
        print("Email: " + str(self.email))
        print("Birthdate: " + str(self.bd))

def show_phonebook():
    """Print all contacts in the phonebook."""
    for (name, contact) in phonebook.items():
        print(name, 'tlf:', contact.phonenumber)
        print(name, 'email:', contact.email)
        print(name, 'birthdate:', contact.bd)

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
            name = input ('add name: ')
            while name in phonebook: 
                print("this name does already exist")
                name = input ('add New name: ')
            phonenumber = input ('add new number: ')
            email = input('Add contacts email:')
            bd = input ('add contacts birthdate')
            phonebook[name] = Contact(phonenumber, email, bd)
            print("Contact has been added to your phonebook")
        elif i == 3:
            name = input('type contact name you wish to delete: ')
            if name in phonebook:
                 del phonebook[name]
                 print ("Contact has been deleted")
            else: 
                print("Try again")
        elif i == 4:
            name = input ('search name: ')
            result= dict((phone_val,phone_k) for phone_val,phone_k in phonebook.items()).get(name)
            print(name, 'phonenumber is:',result.phonenumber)
            print(name, 'email is:',result.email)
            print(name, 'birthdate is:',result.bd)
if __name__ == "__main__":
    main()