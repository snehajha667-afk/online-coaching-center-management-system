class Subject:
    def __init__(self, subject_name, duration, fees):
        self.subject_name = subject_name
        self.duration = duration
        self.fees = fees

    def display_subject(self):
        print("\n------ Subject Details ------")
        print(f"Subject Name : {self.subject_name}")
        print(f"Duration     : {self.duration}")
        print(f"Fees         : ₹{self.fees}")
