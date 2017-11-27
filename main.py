import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def occupationCount():
    histogramData = {}
    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            if row[2] not in histogramData:
                histogramData[row[2]] = 1
            else:
                histogramData[row[2]] += 1
    # print(histogramData)
    jobLabels = histogramData.keys()
    jobCount = histogramData.values()

    y_pos = np.arange(len(jobLabels))
    plt.bar(y_pos, jobCount, align='center', alpha=2.0)
    plt.xticks(y_pos, jobLabels, rotation=90, fontsize = 7)
    plt.ylabel("Number of people")
    plt.xlabel("Job Titles")
    plt.title("Number of people in each job title in Chicago")
    plt.show()

def topSalary():
    index = 0
    salaryList = {}
    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            salary = row[6][1:]
            try:
                salary = float(salary)
            except:
                pass

            if type(salary) is float:
                salaryList[index] = float(salary)

            index += 1

    print("Maximum salary in Chicago is: " + str(max(salaryList.values())))

def minSalary():
    index = 0
    salaryList = {}
    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            salary = row[6][1:]
            try:
                salary = float(salary)
            except:
                pass

            if type(salary) is float:
                salaryList[index] = float(salary)

            index += 1

    print("Minimum salary in Chicago is: " + str(min(salaryList.values())))

def totalFemale():
    count = 0

    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            if row[3] == "F":
                count += 1

    print("Total number of females working in this data is: " + str(count))
    return count

def totalMale():
    count = 0

    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            if row[3] == "M":
                count += 1

    print("Total number of males working in this data is: " + str(count))
    return count

def numFemaleOfficers():
    count = 0

    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            if row[1] == "POLICE OFFICER" and row[3] == "F":
                count += 1


    print("Number of Female Officers in Chicago is: " + str(count))


def main():
    ans = True
    while ans:
        print("""
        0.Number of People in each Job (Graph)
        1.Highest Salary
        2.Min Salary
        3.Number of Female Policer Officers
        4.Number of Males
        5.Number of Females
        6.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "0":
            occupationCount()
        elif ans == "1":
            topSalary()
        elif ans == "2":
            minSalary()
        elif ans == "3":
            numFemaleOfficers()
        elif ans == "4":
            totalMale()
        elif ans == "5":
            totalFemale()
        elif ans == "6":
            ans = False
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")


if __name__ == "__main__":
    main()
