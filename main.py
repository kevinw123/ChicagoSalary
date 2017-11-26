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

    print(max(salaryList.values()))

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

    print(min(salaryList.values()))

def main():
    # occupationCount()
    # topSalary()
    minSalary()

if __name__ == "__main__":
    main()
