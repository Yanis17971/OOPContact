class Blank:
    def __init__(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print ("Объект создан")

    def show(self):
        print(self.name,self.phone,mike.address)


class Contact(Blank):
    def __init__(self,name,phone,address,comment):
        super().__init__(name,phone,address)
        self.comment=comment

        
    def show(self):
        print(self.comment,self.address,self.phone,self.name)


mike=Blank("Михаил Булгаков","20327","Москва,Красная площадь")
Vlad=Blank("Владимир Маяковский","38357","Москва,улица Ленина")
Oleg=Contact("Олег","314324","Москва,улица Арбат","ЛАЛА")





Vlad.address="Санкт-Петербург,улица Ленина"


mike.show()
Vlad.show()
Oleg.show()
