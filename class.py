class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        print('My name is {} {}'.format(self.first_name, self.last_name))


class Student(Person):
    def __init__(self, first_name, last_name, student_card_number):
        super().__init__(first_name, last_name)
        self.student_card_number = student_card_number

    def climb_wall(self):
        print('{}, with the student card is {} usually climb walls to get into school every time he was late'.format(
            self.first_name, self.student_card_number)
        )


person1 = Person('Barry', 'Allen')
print(person1.first_name)
print(person1.last_name)
person1.greeting()

student1 = Student('Wally', 'West', 20318231)
student1.climb_wall()
