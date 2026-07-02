from person import Person


class Student(Person):

    def __init__(self, name, age, phone, email,
                 roll_no, course, subject):

        super().__init__(name, age, phone, email)

        self.roll_no = roll_no
        self.course = course
        self.subject = subject

    def display_student(self):
        print("\n========== Student Details ==========")
        self.display_person()
        print(f"Roll Number : {self.roll_no}")
        print(f"Course      : {self.course}")
        print(f"Subject     : {self.subject.subject_name}")
        print(f"Duration    : {self.subject.duration}")
        print(f"Fees        : ₹{self.subject.fees}")
