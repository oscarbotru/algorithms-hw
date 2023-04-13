import csv
import glob


def get_data_from_file(filename):
    file_data = list()
    with open(filename, 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        for row in dict_reader:
            file_data.append(row)
    return file_data


def show_help():
    print('Welcome to reports builder')
    print('For get report enter number: 1')
    print('For exit enter:              0')


def file_chooser():

    file_list = []
    for file in glob.glob("data/*.csv"):
        file_list.append(file)
    i = 1
    for file_item in file_list:
        print(f"{i}. {file_item.split('/')[:1][0]}")
        i += 1
    while True:
        file_number = input('Enter file number to choose: ')
        try:
            file_number = int(file_number)
            if file_number <= len(file_list):
                return file_list[file_number - 1]
            else:
                print(f'Number must be between 1 and {len(file_list)}')
        except ValueError:
            print('Number of file should be NUMBER')


def get_top_count():
    while True:
        top_count = input('Enter count of rows in report: ')
        try:
            top_count = int(top_count)
            return top_count
        except ValueError:
            print('Number of file should be NUMBER')


def get_field_for_sort():
    print('You can choose sort by date - 1, or amount - 2')
    while True:
        field_number = input('Enter number of field: ')
        try:
            field_number = int(field_number)
            return field_number
        except ValueError:
            print('Number of file should be NUMBER')


def get_type_of_sorting(algorithms_list):
    print('You can choose algorith for sort:')
    i = 1
    for alg in algorithms_list:
        print(f"{i}. {alg}")
        i += 1
    while True:
        alg_number = input('Enter file number to choose: ')
        try:
            alg_number = int(alg_number)
            if alg_number <= len(algorithms_list):
                return algorithms_list[alg_number - 1]
            else:
                print(f'Number must be between 1 and {len(algorithms_list)}')
        except ValueError:
            print('Number of file should be NUMBER')

