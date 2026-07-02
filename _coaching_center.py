from coaching_center import CoachingCenter

center = CoachingCenter()

while True:
    print("\n========== ONLINE COACHING MANAGEMENT SYSTEM ==========")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Student")
    print("4. View Students")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Add Teacher")
    print("8. View Teachers")
    print("9. Search Teacher")
    print("10. Delete Teacher")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        center.add_subject()

    elif choice == "2":
        center.view_subjects()

    elif choice == "3":
        center.add_student()

    elif choice == "4":
        center.view_students()

    elif choice == "5":
        center.search_student(input("Enter Roll Number: "))

    elif choice == "6":
        center.delete_student(input("Enter Roll Number: "))

    elif choice == "7":
        center.add_teacher()

    elif choice == "8":
        center.view_teachers()

    elif choice == "9":
        center.search_teacher(input("Enter Teacher ID: "))

    elif choice == "10":
        center.delete_teacher(input("Enter Teacher ID: "))

    elif choice == "11":
        print("Thank you for using Online Coaching Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")
