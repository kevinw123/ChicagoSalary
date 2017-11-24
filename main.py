import csv
import matplotlib.pyplot as plt

def main():
    with open("chicago_salaries.csv") as csvfile:
        employeeRow = csv.reader(csvfile, delimiter=",")
        for row in employeeRow:
            print(row)

if __name__ == "__main__":
    main()
