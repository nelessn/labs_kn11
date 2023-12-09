class human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        a = print('name: ', self.name, 'age:', self.age, "height:", self.height)
        
class student(human):
    grade = None

    def __init__(self, name, age, height, grade):
        super().__init__(name, age, height)
        self.grade = grade

    def get_info(self):
        super().get_info()
        print('grade: ', self.grade)

class musician(human):
    instrument = None

    def __init__(self, name, age, height, instrument):
        super().__init__(name, age, height)
        self.instrument = instrument
        
    def get_info(self):
        super().get_info()
        print('instrument: ', self.instrument)

class parent(human):
    pass

student = student('Mike', 19, 180, 4)
musician = musician('Han', 23, 169, 'guitar')
parent = parent('Olan', 35, 176)
student.get_info()
musician.get_info()
parent.get_info()