# Christiana Huss
# CIS 129
# Module 11 Lab
# 07/20/24
# Programs for 9.1, 9.2, and 9.3 

# 9.1 - WRITE GRADES TO PLAIN TEXT FILE 
# User to input # of grade entries they want
# for loop to iterate through and enter each
# with open as file to write to text file 
# close the file 

#initialize empty grade list 
grade_list = [] 

# message to user to indicate what stage of the code we're at 
print("We will first be entering grades into a text file to calculate their average.")

# user to indicate how many grades they'll be entering 
n = int(input("How many grades would you like to enter?"))

# for loop for user to enter desired number of grades 
for i in range(n):
    grade = float(input(f"Enter grade {i+1}: "))
    grade_list.append(grade) # add each input to the array 

# print the list back to user 
print("The grades you entered are: ", grade_list)

# create new text file to write grades to 
with open('grades.txt', mode = 'w') as file:
    for grade in grade_list: 
        file.write(f'{grade}\n')
        
file.close 

# 9.2 - READ GRADES FROM PLAIN TEXT FILE 
# with open as file to open text file in read mode 
    # get len(list) to get count
    # for loop to convert each text file grade entry to a float 
        # total = total + each grade 
    # average = total/count 
# print total, count, and average back to user 

with open('grades.txt', mode = 'r') as file:
    grade_list_output = file.readlines() 
    count = len(grade_list_output)
    print(f'You entered {count} grades. Wahoo!')

    total = 0
    i = 1
    for grade in grade_list_output:
        grade_float = float(grade)

        total += grade_float
        i+=1

    average = total/count 
    print(f'The total sum of your {count} grades is {total}. The average of these grades is {average}.')
    
# 9.3 - WRITE STUDENT RECORDS TO A CSV FILE
# import csv to create new csv file 
# for loop to iterate through user-input number of entries
    # input first name, last name, 3 grades 
    # store this data in a dictionary 
    # add each dictionary to an array 
# define dictionary fields to create csv file 
# name csv file 
# with open as csvfile 
    # call dictwriter, writeheader, writerows to write data to csv file 

import csv

# message to user to indicate what stage of the code we're at 
print("We will now be entering student names and 3 grades from the semester into a CSV file.")

# User to input how many student entries they have 
entries = int(input("How many student entries do you have?"))

# Create list to store student data dictionaries 
student_list = []

# For loop to get names and 3 grades for each student 
for j in range(entries):
    first = str(input(f"Enter student {j+1}'s first name: "))
    last = str(input(f"Enter student {j+1}'s last name: "))
    grade1 = int(input(f"Please enter grade 1: "))
    grade2 = int(input(f"Please enter grade 2: "))
    grade3 = int(input(f"Please enter grade 3: "))

    # Create dictionary to store 
    student_dict = {
        "First Name": first, 
        "Last Name": last, 
        "Grade 1": grade1,
        "Grade 2": grade2,
        "Grade 3": grade3,
    }

    # add each dictionary item to student list array 
    student_list.append(student_dict) 

    # print student dict after creating 
    print(student_dict) 

# format data to create CSV file 
fields = ['First Name', 'Last Name', 'Grade 1', 'Grade 2', 'Grade 3']

# name of csv file
filename = "grades.csv"

# write data to a csv file 
with open(filename, mode = 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(student_list)

# goodbye message to user 
print("Your data is now stored in the csv file 'grades.csv'. Wahoo!")