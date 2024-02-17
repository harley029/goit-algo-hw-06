
from collections import UserDict, UserList

class Name:
    def __init__(self, name):
        self.name=name

    def SetName(self,name):
        self.name=name
    
    def GetName(self):
        return self.name

class Phone(UserList):

    def NormalizePone(self, phone): # Нормализатор номера телефона
        if len(phone) == 12:
            new_phone = "+" + phone
            return new_phone
        elif len(phone) < 12:
            new_phone = "+38" + phone   
            return new_phone
        return phone

    def SetPhone(self,phone):
        self.data.append(self.NormalizePone(phone))
        return f"Номер {self.NormalizePone(phone)} добавлено."


    def GetPhone(self): # возвращает №-ра телефонов списком -> List
        return self.data
    
    def GetPhones(self): # возвращает №-ра телефонов одной строкой -> Str
        return f"{'; '.join(self)}" 
    
    def DelPhone(self, phone):
        self.data.remove(self.NormalizePone(phone))
        return f"Номер {self.NormalizePone(phone)} видалено."
    
    
    def ChangePhone(self,phone1, phone2):
        self.data.remove(self.NormalizePone(phone1))
        self.SetPhone(phone2)
        return f"Номер {self.NormalizePone(phone1)} було змінено на {self.NormalizePone(phone2)}"

class Record(UserDict, Name, Phone):
    def __init__(self, name, phone):
        self.name=Name(name)
        self.phone=Phone(phone)

    def Setname(self, name:Name):
        self.data['name']=(name)
    
    def GetName(self):
        return self.data.get('name')
    
    def SetPhone(self, phone):
        phone_list = self.data.get('phones', Phone())
        phone_list.data.append(phone)
        self.data['phones'] = phone_list

    def GetPhone(self):
        return self.data.get('phones') 


rec=Record('Alex', '0989399711')
# rec.Setname('Alex')
print(rec)
print(rec.GetName())

rec.SetPhone('0992261935')
rec.SetPhone('0989309711')
print(rec)
print(rec.GetPhone())

# pr=Phone([])
# print(pr.SetPhone('0989309711'))
# print(pr.GetPhone())
# print(pr.GetPhones())
# pr.SetPhone('0957654532')
# print(pr.GetPhones())
# pr.SetPhone('380976543432')
# print(pr.GetPhones())
# print(pr.DelPhone('0989309711'))
# print(pr.GetPhones())
# print(pr[1])
# print(pr.ChangePhone('0976543432', '0992261935'))
# print(pr.GetPhones())
# print()

# nm=Name()
# nm.SetName('Onix')
# print(nm.GetName())
# nm.SetName('Lada')
# print(nm.GetName())