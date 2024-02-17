# user -> 
#       user_book ->
#                  records ->
#                           field, field, field

from collections import UserDict, UserList

# class Field:
#     def __init__(self, value) -> None:
#         self.value = value
    
#     def __str__(self):
#         return str(self.value)
    
class Name:
    def __init__ (self, name):
        self.name = name

    def SetName(self,name):
        self.name=name
    
    def GetName(self):
        return self.name

class Phone(UserList):
    def __init__ (self, phone):
        self.phone = phone

    def SetPhone(self,phone):
        if len(phone) == 12:
            new_phone = "+" + phone
        elif len(phone) < 12:
            new_phone = "+38" + phone
        self.data.append(new_phone)

    def GetPhone(self):
        return self.data
    
    def GetPhones(self): # возвращает №-ра телефонов одной строкой
        return f"{'; '.join(self.phone.GetPhone())}" 
    
class Record(UserDict):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phone([])
    
class AddressBook:
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

counter=0
def add_contact(args, contacts):
    global counter
    # contacts[counter]=Record(args[0].SetName(),args[1].SetPhone())
    contacts.SetName = args[0]
    contacts.SetPhone = args[1]
    # contacts=args[0], args[1]
    print(contacts)
    counter+=1

def main():
    contacts = Record({})
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
# for i in range(len(phone.GetPhone())):
#     print(phone[i])
# print(f"Phones: {'; '.join(phone.GetPhone())}")
# print(phone.GetPhones())
