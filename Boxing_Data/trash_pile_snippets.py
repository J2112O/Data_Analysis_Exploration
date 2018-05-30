#!/usr/bin/python3.6
import csv


def main():
    with open('clean_bouts_out.csv', 'r') as boxer_file:
        csv_reader = csv.reader(boxer_file)
        header = next(csv_reader)
        data = []
        for row in csv_reader:
            print(row[0])


if __name__ == '__main__':
    main()
