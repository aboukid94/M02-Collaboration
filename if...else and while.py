#Nicholas Abouhalkah

#Grade Point Average system
#This program will allow you to verify a student's academic recognition.
#SDEV 220


print("Welcome! Please enter the following information. ")

#This is the start of the loop.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")

#This ends the loop if the name is ZZZ

    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))


#Grade Point Average calculator.
    if GPA >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List! Congratulations!")
    elif GPA >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll! Congratulations!")
    else:
        print(f"{first_name} {last_name} does not qualify for either. Better luck next time!")