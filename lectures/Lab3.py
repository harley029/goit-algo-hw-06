class Contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.email=''
        self.cols=[10,7,30]

    def setColWidth(self,cols):
        self.cols=cols
        
    def setPhone(self,phone):
        self.phone=phone

    def setName(self,name):
        self.name=name
    
    def setEmail(self,email):
        self.email=email

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone
    
    def getName(self):
        return self.name
    
    def print(self):
        print(f"{self.name:(self.cols[0])} : {self.phone} : {self.email}")

    def getContact(self):
        return f"{self.name:10} : {self.phone} : {self.email}"
    
    def getContactAsCSV(self):
        return f"{self.name},{self.phone},{self.email}\n"
    def getContactAsTSV(self):
        return f"{self.name}\t{self.phone}\t{self.email}\n"
'''
adssdasd
'''
counter=0

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    global counter
    contacts[counter]=Contact(args[0],args[1])
    counter+=1

def change_phone(args,contacts):
    contacts[int(args[0])].setPhone(args[1])
    return f"Phone for record {args[0]} changed to {args[1]}"

def change_name(args,contacts):
    contacts[int(args[0])].setName(args[1])

def setEmail(args,contacts):
    contacts[int(args[0])].setEmail(args[1])


def print_phones(args,contacts):
    for key in contacts:
        contacts[key].print()

def changeColWidth(args,contacts):
    for contact in contacts.values():
        contact.setColWidth([int(i) for i in args])
    
def listAll(contacts):
    for key in contacts:
        print(contacts[key].getContact())
    
def writeToCSV(args,contacts):
    with open(args[0],"w+") as csvfile:
        for key in contacts:
            csvfile.write(contacts[key].getContactAsCSV())
    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "changephone":
            print(change_phone(args, contacts))
        elif command == "changename":
            print(change_name(args, contacts))

        elif command == "width":
            print(changeColWidth(args, contacts))
        elif command == "mail":
            print(setEmail(args, contacts))

        elif command == "print":
            print(print_phones(args, contacts))
        elif command == "list":
            print(listAll(contacts))                   
        elif command == "tocsv":
            print(writeToCSV(args,contacts))                   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()