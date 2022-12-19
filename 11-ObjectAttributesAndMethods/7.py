class Student():
    university = "UEK Kraków"
    id = 100000

    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Student.id
        Student.id += 1
    def __str__(self):
        return f" {self.name} {self.surname} ({Student.id}), {self.field},{Student.university}"
 
student1 = Student("Jan", "Kubiena", "Informatyka")
print(student1)
student2 = Student("Janusz", "Khdkdkd", "Informatyka")
print(student2)