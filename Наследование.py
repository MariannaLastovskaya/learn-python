
class QA():
    #Класс по описанию тестировщика
    def __init__(self, grade, type, role):
    #Инициализация атрибутов тестировщика

        self.grade = grade
        self.type = type
        self.role = role
    def description_name(self):
    #Возвращаем описание тестировщика
        desc = self.grade + ' ' + self.type + ' ' + self.role
        return desc.title()

Anna = QA('junior', 'manual','idle') #экземпляр класса
    #print (Anna.description_name())

class Dev(QA): #наследование от класса QA
    #Аспекты характерные для программистов
    def __init__(self, grade, type, role):
    #Инициализация атрибутов класса родителя
        super().__init__(grade, type, role) #помогает связать потомка и родителя
        self.year = 18

    def description_year(self):
    #выводит информацию об ОС с которой работает программист
        print("Этому программисту " + str(self.year) + " лет")

    #переопределение родительского метода
    def description_name(self):
    #Возвращаем описание тестировщика
        desc = self.grade + ' ' + self.type
        return desc.title()

Valera = Dev('junior', 'c++', 'ci')
print(Valera.description_name())
Valera.description_year()



