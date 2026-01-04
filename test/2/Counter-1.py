# Program to create and read underperform.csv file

import csv

# opening the file in write mode
file = open("underperform.csv", "w", newline="")

writer = csv.writer(file)

# writing header row
writer.writerow(["SID", "SNAME", "INTERNAL", "EXTERNAL"])

# accepting number of students
n = int(input("Enter number of students: "))

# taking student details
for i in range(n):
    sid = input("Enter Student ID: ")
    sname = input("Enter Student Name: ")
    internal = int(input("Enter Internal Marks: "))
    external = int(input("Enter External Marks: "))
    
    writer.writerow([sid, sname, internal, external])

# closing file after writing
file.close()

print("\nDetails stored successfully.\n")

# opening the file in read mode
file = open("underperform.csv", "r")

reader = csv.reader(file)

# skipping header
next(reader)

print("Students who scored less than 40 total marks:")
print("SID\tSNAME")

# reading each row
for row in reader:
    total = int(row[2]) + int(row[3])
    
    if total < 40:
        print(row[0], "\t", row[1])

# closing file
file.close()
