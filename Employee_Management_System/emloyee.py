import tkinter as t
r = t.Tk()
r.title('Employee Management System')
button = t.Button(r, text='PRESS TO START', width=65, command=r.destroy)
button.pack()
r.mainloop()


def emp_info(emp_name1, emp_fam1, emp_age1, id1):  # function used to save full name and age
    name = input("Enter the employee's name:")                        # k is the default id
    family = input("Enter the employee's family name:")               # id1 is the employees id
    birth = int(input("Enter the employee's year of birth:"))    # year is the current year
    if birth < 2000:
        age = (2000-birth)+(year-2000)
    else:
        age = year-birth
    if age >= 63 or age < 18:
        print("We are so sorry this employee cant apply for this job")
        return False
    else:                                                       # if smaller than 63 the employee is info is added
        emp_name1.insert(id1 - k, name)
        emp_fam1.insert(id1 - k, family)
        emp_age1.insert(id1 - k, age)
        return True


def emp_info2(emp_salary1, emp_shift1, emp_shift2, emp_shift0, id2):  # function used to save the salary and shift
    shift1 = int(input("Enter the employee's shift starting hour:"))
    shift2 = int(input("Enter the employee's shift ending hour:"))
    emp_shift1.insert(id2-k, shift1)
    emp_shift2.insert(id2-k, shift2)
    shift0 = (12-shift1) + shift2
    emp_shift0.insert(id2-k, shift0)
    salary = int(input("Enter the employee's salary:"))
    emp_salary1.insert(id2-k, salary)


def id_generator(year1, number):  # Generates the admin\starting ID (According to the year and number of employees)
    for h in range(1, 6):
        if number < 10**h:
            return year1*10**h


def emp_rem_info1(emp_name5, emp_fam2, emp_age2, rem_emp2):       # removes the employees information_1
    emp_name5.pop(rem_emp2)
    emp_fam2.pop(rem_emp2)
    emp_age2.pop(rem_emp2)


def emp_remove_info2(emp_salary1, emp_shift1, emp_shift2, emp_shift0, rem_emp2):   # removes the employees information_2
    emp_shift1.pop(rem_emp2)
    emp_shift2.pop(rem_emp2)
    emp_shift0.pop(rem_emp2)
    emp_salary1.pop(rem_emp2)


def emp_replacer(emp_name4, emp_fam3, emp_age3, emp_salary3, emp_shift1, emp_shift2, emp_shift0, replace_id):
    check = emp_info(emp_name4, emp_fam3, emp_age3, replace_id)
    if check:  # checks if the employee is smaller than 63
        emp_info2(emp_salary3, emp_shift1, emp_shift2, emp_shift0, replace_id)
    return check


def admin_rep():                                   # instead of writing the input\print statement multiple times
    admin1 = input("""\nEnter 'ADD' or 'add' to add a new employee; 
Enter 'REMOVE' or 'remove' to remove an existing employee;
Enter 'REVIEW' or 'review' to review the existing employee's information;
Enter 'INBOX' or 'inbox' to view your inbox;
Enter 'PW' or 'pw' to change your password;
Enter 'end' to exit : """)
    return admin1


def emp_pass():
    list1 = []
    password = ""
    list1.append(chr(random.randrange(65, 91)))
    list1.append(chr(random.randrange(97, 123)))
    list1.append(chr(random.randrange(42, 48)))
    list1.append(chr(random.randrange(48, 58)))
    random.shuffle(list1)
    for character in range(len(list1)):
        password += list1[character]
    return password


print("Hello Admin!")
year = int(input("Enter the current year:"))
emp_number = int(input("Enter the number of employees needed:"))
k = id_generator(year, emp_number)    # main ID
print("Your ID is:", k, "\nYour Password is: '0000'")
sec_id = input("Please enter your ID,-1 to end:")
id0 = int(sec_id)                # employee's ID
n_id = k
emp_name = ["admin"]             # used to store the names of the users
emp_family = ["admin"]           # used to store the family of the users
emp_age = [0]                    # used to store the age of the users
emp_salary = [0]                 # used to store the salary of the users
emp_shift = [0]                  # used to store the Total shift of the users
emp_shift_m = [0]                # used to store the morning shift of the users
emp_shift_n = [0]                # used to store the noon shift of the users
emp_login = [0 for f in range(0, emp_number)]        # used to store the login info of the users
workers = 0                      # the number of total employees
remove = False  # In order to replace the employee removed
rem_emp = 0
account_info = {k: "0000"}       # used to store the password of the users
emp_mess = {}

while id0 != -1:                 # Program loop
    import random
    pw = input("Enter your password:")

    if id0 == k and pw == account_info[k]:          # ADMIN
        print("Welcome admin!")
        admin = admin_rep()

        while admin != "end":

            if admin == "ADD" or admin == "add":    # calls the employee info adders
                if remove:
                    print("The employee of ID", rem_emp + k, "is removed!")
                    print("The employee of ID", rem_emp + k, "is to be replaced!")

                    adult = emp_replacer(emp_name, emp_family, emp_age, emp_salary, emp_shift_m, emp_shift_n,
                                         emp_shift, rem_emp + k)
                    if adult:                # checks if the employee that is replacing the removed one is old enough
                        emp_rem_info1(emp_name, emp_family, emp_age, rem_emp+1)
                        emp_remove_info2(emp_salary, emp_shift_m, emp_shift_n, emp_shift, rem_emp+1)
                        remove = False                                                # sets "remove" back to false
                        account_info[rem_emp + k] += str(random.randrange(10))
                        account_info[rem_emp + k] += chr(random.randrange(48, 58))
                        print("The employee's ID is:", rem_emp+k)
                        print("The employee's  new password is:", account_info[rem_emp + k])
                        emp_login[rem_emp] = 0    # set the login status back to 0
                        admin = admin_rep()
                    else:
                        continue

                else:                          # employee adding
                    adult2 = emp_replacer(emp_name, emp_family, emp_age, emp_salary, emp_shift_m, emp_shift_n,
                                          emp_shift, n_id + 1)
                    if adult2:
                        n_id += 1  # The id adds 1 for each workers id to generate his\her id
                        workers += 1                                      # increments workers by 1
                        account_info[n_id] = emp_pass()
                        print("The employee's ID is:", n_id)
                        print("The employee's password is:", account_info[n_id])
                    admin = admin_rep()

            elif (admin == "REMOVE") or (admin == "remove"):

                id_remove = int(input("Enter the ID of the employee to be removed:"))

                while (id_remove > (workers+k)) and (id_remove < k):            # asks the user to enter an existing ID
                    print("This employee's ID doesnt exist!")
                    id_remove = int(input("Enter the ID of the employee to be removed:"))

                rem_emp = id_remove-k
                admin = "ADD"
                remove = True
                continue

            elif admin == "REVIEW" or admin == "review":

                print("Employee ID | First Name | Family Name | Age | Salary | Shift | Start |  End  | Password |login \
                |")
                for x in range(1, workers+1):
                    print("%-9d   " % (x + k), " %-10s " % emp_name[x], " %-11s " % emp_family[x],
                          " %-3d " % emp_age[x],
                          " %-6d " % emp_salary[x], " %2dHrs " % emp_shift[x], " %2d:00 " % emp_shift_m[x],
                          " %2d:00 " % emp_shift_n[x], " %-8s " % account_info[x + k], " %-4d |" % emp_login[x],
                          sep="|")
                admin = admin_rep()
            elif admin == "INBOX" or admin == "inbox":
                if len(emp_mess) != 0:
                    for emp, mess in emp_mess.items():
                        print(len(emp_mess[emp])*"-"*3)
                        print(mess)
                        print("Source:", emp_name[emp-k], emp_family[emp-k], " of the ID:", emp, ".")
                        print(len(emp_mess[emp]) * 3 * "-")
                    emp_mess = {}
                else:
                    print("Your inbox is empty!")

                admin = admin_rep()

            elif admin == "PW" or admin == "pw":
                account_info[id0] = input("Enter your new password:")
                admin = admin_rep()

    elif k < id0 <= k+workers and pw == account_info[id0]:         # EMPLOYEES
        if emp_login[id0-k] == 0:
            employee = "pw"
            emp_login[id0 - k] += 1
        else:
            emp_login[id0 - k] += 1
            employee = input("\nEnter 'REVIEW' or 'review' to review your info;"
                             + "\nEnter 'PW' or 'pw' to change your password;"
                             + "\nEnter 'MESSAGE' or 'message' to send the admin a message;"
                             + "\nEnter 'end' to exit:")
        while employee != "end":
            z = id0 - k
            if employee == "REVIEW" or employee == "review":
                print("""\nYour ID    | First Name | Family Name | Age | Salary | Shift | Start |  End  | Password |""")
                print("%-9d  " % id0, " %-10s " % emp_name[z], " %-11s " % emp_family[z], " %-3d " % emp_age[z],
                      " %-6d " % emp_salary[z], " %2dHrs " % emp_shift[z], " %2d:00 " % emp_shift_m[z],
                      " %2d:00 " % emp_shift_n[z], " %-8s |" % account_info[id0], sep="|")

            elif employee == "PW" or employee == "pw":
                account_info[id0] = input("Enter your new password:")

            elif employee == "MESSAGE" or employee == "message":
                emp_mess[id0] = (input("Enter Your message:"))

            employee = input("\nEnter 'REVIEW' or 'review' to review your info;"
                             + "\nEnter 'PW' or 'pw' to change your password;"
                             + "\nEnter 'MESSAGE' or 'message' to send the admin a message;"
                             + "\nEnter 'end' to exit:")
    else:
        print("Your ID or password is invalid!")

    id0 = int(input("Please enter your ID,-1 to end:"))
