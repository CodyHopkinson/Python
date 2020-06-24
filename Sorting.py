students_present = ["caesar", "carly", "braeden", "joseph", "cody", "marley", "bruno"]
students_absent = ["stephen", "benny", "jade", "dio", "natsuki", "giorno"]

print("Students Present: ")

students_present.sort()

for student in students_present:
    print(student.title())

print("\nStudents Absent: ")

students_absent.sort()

for student in students_absent:
    print(student.title())
