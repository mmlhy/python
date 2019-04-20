class Person:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
class AddressBook:
    def __init__(self):
        self.persons = []
    def addPerson(self,person):
        self.persons.append(person)
    def delPerson(self,person):
        i=0
        for pp in self.persons:
            if pp.name == person:
                del self.persons[i]
                break
            i=i+1
    def queryPerson(self,person):
        i = 0
        for pp in self.persons:
            if pp.name == person:
                print("名字：",pp.name)
                print("地址：",pp.address)
                print("电话：",pp.phone)
                break
            i = i + 1
    def listAllPerson(self):
        for pp in self.persons:
                print("名字：",pp.name)
                print("地址：",pp.address)
                print("电话：",pp.phone)
addressBook = AddressBook()
while True:
    print("1.创建联系人")
    print("2.删除联系人")
    print("3.查询联系人")
    print("4.列出所有联系人")
    m = int(input("输入要选择的功能："))
    if m == 1:
        name = input("输入名字：")
        address = input("输入地址:")
        phone = input("输入电话号:")
        p = Person(name,address,phone)
        addressBook.addPerson(p)
    if m == 2:
        name = input("要删除的名字:")
        addressBook.delPerson(name)
    if m == 3:
        name = input("要查询的名字:")
        addressBook.queryPerson(name)
    if m == 4:
        addressBook.listAllPerson()
