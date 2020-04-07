import reading_from_user

def get_details(): #get the details from the user i.e. the login name and password
    name = reading_from_user.read_nonempty_alphabetical_string("Name: ")
    password = reading_from_user.read_nonempty_string("Password: ")
    names_list, password_list = read_file("details.txt")

    if name in names_list and password in password_list:
        position = names_list.index(name)
        position_password = password_list.index(password)
        if position == position_password:
            return name
        else:
            print("\nModule Record System - Login Failed")
    else:
        print("\nModule Record System - Login Failed")

def read_file(name_of_file): #I used this to open the file details and modules and return two lists
    list1 = []
    list2 = []
    connection = open(name_of_file, "r")
    while True:
        line = connection.readline()
        line = line.rstrip()
        if line == "":
            break
        else:
            line = line.split(" , ")
        list1.append(line[0])
        list2.append(line[1])
    connection.close()
    return list1, list2

def get_menu(): #This is used to print the menu
    print("\nModule Record System - Options")
    print("-"*30)
    print("1. Record Attendence\n2. Generate Statistics\n3. Exit")

def only_number(prompt, fixed_number): #This is used to validate a specific input of a number in a certain range
    fixed_number = fixed_number + 1
    list1 = []
    i = 1
    while i < fixed_number:
        list1.append(i)
        i = i + 1

    while True:
        try:
            number = int(input(prompt))
            if number in list1:
                return number
            else:
                print("Please input the correct range")
        except ValueError:
            print("Put in a number.")

def main(): #This includes the repetition of the menu and welcomes the user
    while True:
        name = get_details()

        if name is not None:
            print(f"\nWelcome {name}")

            while True:
                get_menu()
                number = only_number(">>> ", 3)

                if number == 1:
                    code_list, modules_list, choice = load_modules("Attendance")
                    names, present, absent, excused = get_class_attendence(choice)
                    take_class_attendence(names, present, absent, excused, choice)

                elif number == 2:
                    generate_and_save_stats()

                else:
                    print("\nThank you! Take care!")
                    break
            break
        else:
            break

main()