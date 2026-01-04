# Program to maintain CS student scores using binary file

import pickle

# function to add a new student record
def add_record():
    file = open("cs_scores.dat", "ab")
    
    sid = int(input("Enter Student ID: "))
    sname = input("Enter Student Name: ")
    mark = int(input("Enter Marks: "))
    
    record = [sid, sname, mark]
    pickle.dump(record, file)
    
    file.close()
    print("Record added successfully.\n")


# function to increment marks of all students by 5
def increment_marks():
    file = open("cs_scores.dat", "rb")
    temp = []

    print("\nMarks updated for following students:")
    print("SID\tSNAME\tOLD\tNEW")

    try:
        while True:
            record = pickle.load(file)
            
            old_mark = record;
            old_mark = record[2]
            record[2] = record[2] + 5
            
            print(record[0], "\t", record[1], "\t", old_mark, "\t", record[2])
            
            temp.append(record)
    except EOFError:
        file.close()

    file = open("cs_scores.dat", "wb")
    for r in temp:
        pickle.dump(r, file)

    file.close()
    print("\nMarks incremented by 5 for all students.\n")



# function to display all records
def display_records():
    file = open("cs_scores.dat", "rb")
    
    print("SID\tSNAME\tMARK")
    
    try:
        while True:
            record = pickle.load(file)
            print(record[0], "\t", record[1], "\t", record[2])
    except EOFError:
        file.close()


# menu driven program
while True:
    print("\n1. Add Record")
    print("2. Increment Marks by 5")
    print("3. Display Records")
    print("4. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        add_record()
    elif ch == 2:
        increment_marks()
    elif ch == 3:
        display_records()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
