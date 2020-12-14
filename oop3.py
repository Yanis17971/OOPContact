class Human:
    def __init__(self,name):
        self.name=name

    def answer_question(self,question):
        print("Очень интересный вопрос! Не знаю")


class Student(Human):
    def ask_question(self,someone,question):
        print(someone.name,question)
        someone.answer_question(question)
        print()

class Curator(Human):
    def answer_question(self,question):
        if question=="Мне грустно,что делать?":
            print("Держись всё получится,щас скину видео с котиками")
        else:
            super().answer_question(question)

class Teacher(Human):
    def answer_question(self,question):
        if question=="Что не так с моим проектом?":
            print("О вопроос про проект,это я люблю!")
        else:
            super().answer_question(question)

class Intern(Student):
    def answer_question(self,question):
        if question=="Ты стажёр?":
            print("Да")
        else:
            super().answer_question(question)


student=Student("Тимофей")
curator=Curator("Мария")
teacher=Teacher("Евгений")
intern=Intern("Виталий")
friend=Human("Дима")


student.ask_question(curator,"Мне грустно,что делать?")
student.ask_question(teacher,"Что не так с моим проектом?")
student.ask_question(teacher,"Когда каникулы?")
student.ask_question(intern,"Что не так с моим проектом?")
student.ask_question(intern,"Ты стажёр?")
student.ask_question(friend,"Как устроится работать питонистом?")
intern.ask_question(teacher,"Что не так с моим проектом?")
