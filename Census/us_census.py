#!/usr/bin/python3.6
import csv


def main():

    file = ('acs2015_county_data.csv')
    with open(file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data_set = [row for row in csv_reader]
        print(header)
        print(data_set[0])


if __name__ == '__main__':
    main()
