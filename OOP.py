class Blank:
    def __init__(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print ("Объект создан")


mike=Blank("Михаил Булгаков","20327","Москва,Красная площадь")
Vlad=Blank("Владимир Маяковский","38357","Москва,улица Ленина")
Oleg=Blank("Олег","314324","Москва,улица Арбат")

def print_contact():
    print(mike.name,mike.phone,mike.address)
    print(Vlad.name,Vlad.phone,Vlad.address)
    print(Oleg.name,Oleg.phone,Oleg.address)



Vlad.address="Санкт-Петербург,улица Ленина"


print_contact()
