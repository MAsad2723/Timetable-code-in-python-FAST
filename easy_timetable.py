import pandas as pd
import numpy as np
import openpyxl
# row = 47
# cols = 9
def isnan(str):
    return str!=str
def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
print("Welcome to the FAST TimeTable\n")
print("Enter the day you want TimeTable of: \n")
print("1: Monday\n")
print("2: Tuesday\n")
print("3: Wednesday\n")
print("4: Thursday\n")
print("5: Friday\n")
day = int(input())
if day == 1:
    file = pd.read_excel('FAST School of Computing - Fall 2023 TimeTable.xlsx', sheet_name='MONDAY')
elif day == 2:
    file = pd.read_excel('FAST School of Computing - Fall 2023 TimeTable.xlsx', sheet_name='TUESDAY')
elif day == 3:
    file = pd.read_excel('FAST School of Computing - Fall 2023 TimeTable.xlsx', sheet_name='WEDNESDAY')
elif day == 4:
    file = pd.read_excel('FAST School of Computing - Fall 2023 TimeTable.xlsx', sheet_name='THURSDAY')
elif day == 5:
    file = pd.read_excel('FAST School of Computing - Fall 2023 TimeTable.xlsx', sheet_name='FRIDAY')

row, cols = file.shape

file = np.array(file)
name_of_subjects = {}
total_subjects = {}
array2 = {}
count = 0
for i in range(cols):
    for j in range(row):
        if i > 0 and j > 2 and (not isnan(file[j][i])):
            total_subjects[count] = file[j][i]
            count+=1
bubbleSort(total_subjects)
print("Enter your section name: [BCS-**]\n")
subjects = str(input())
# subjects = "BCS-5G"
a = "h"
count = 0
for i in range(cols):
    for j in range(row):
        a = str(file[j][i])
        if a.find(subjects) != -1:
            array2[count] = "Time:\t" + file[1][i] + "\n" + file[j][i] + "\n" + "Venue:\t" + file[j][0] + "\n"
            count+=1
print("Enter number of electives you have taken: (Type 0 if you have none): ")
num = int(input())
for i in range(num):
    print("Enter your section name: [BCS-**]\n")
    section = str(input())
    print("Enter your Elective name: [ME/Psych etc]\n")
    subject = str(input())
    subject=subject+" "+section
    for i in range(cols):
        for j in range(row):
            a = str(file[j][i])
            if a.find(subject) != -1:
                array2[count] = "Time:\t" + file[1][i] + "\n" + file[j][i] + "\n" + "Venue:\t" + file[j][0] + "\n"
                count+=1
# bubbleSort(array2)

print("Your Required timetable is: \n")
for i in array2:
    print(array2[i])
input()
input()
input()
# Written by M.Asad