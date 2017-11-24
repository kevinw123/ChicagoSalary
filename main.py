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
    plt.xticks(y_pos, jobLabels)
    plt.ylabel("Number of people")
    plt.xlabel("Job Titles")
    plt.title("Number of people in each job title in Chicago")
    plt.show()

def main():
    occupationCount()

if __name__ == "__main__":
    main()
