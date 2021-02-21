
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def print_person(self):
        print(self.firstname+' '+self.lastname)


class Student(Person):
    def __init__(self, firstname, lastname, subject): 
        Person.__init__(self,firstname, lastname ) 
        self.subject = subject
    def print_student(self):
        print(self.firstname+' '+self.lastname +'\n'+'Subject area: ' + self.subject)
