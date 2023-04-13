from bubble_sort import bubble_sort
from quick_sort import quick_sort
from utils import show_help, file_chooser, get_top_count, get_field_for_sort, get_type_of_sorting


def main():
    algorithms_list = [
        'quick',
        'bubble'
    ]
    while True:
        show_help()
        command_number = input('Enter command number: ')
        try:
            command_number = int(command_number)
            if command_number == 0:
                break
            elif command_number == 1:
                chosen_file = file_chooser()
                top_count = get_top_count()
                sort_field = get_field_for_sort()
                chosen_algorithm = get_type_of_sorting(algorithms_list)
                result = list()
                if chosen_algorithm == 'quick':
                    result = quick_sort(chosen_file, top_count, sort_field)
                elif chosen_algorithm == 'quick':
                    result = bubble_sort(chosen_file, top_count, sort_field)
                print('*' * 50)
                print('Here is result:')
                print(result)
                break
            else:
                print('Unknown command number')
        except ValueError:
            print('Command number must be NUMBER')
    print('=' * 50)
    print('Thank you for using our report builder')


if __name__ == '__main__':
    main()
