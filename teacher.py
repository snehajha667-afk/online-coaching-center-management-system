from person import Person


class Teacher(Person):

    def __init__(self, name, age, phone, email,
                 teacher_id, qualification,
                 experience, subject):

        super().__init__(name, age, phone, email)

        self.teacher_id = teacher_id
        self.qualification = qualification
        self.experience = experience
        self.subject = subject

    def display_teacher(self):
        print("\n========== Teacher Details ==========")
        self.display_person()
        print(f"Teacher ID   : {self.teacher_id}")
        print(f"Qualification: {self.qualification}")
        print(f"Experience   : {self.experience}")
        print(f"Subject      : {self.subject.subject_name}")
