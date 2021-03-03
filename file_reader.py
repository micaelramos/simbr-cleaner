import csv


def read_file(filename):
    filename = _check_input(filename)
    with open(filename, 'r') as data:
        return [i for i in csv.DictReader(data)]


def _check_input(input_filename):
    with open(input_filename, 'rb') as file:
        csv_format = csv.Sniffer().sniff(str(file.read(1024)))
    if csv_format.delimiter != ',':
        print('Input file does not have a valid delimiter char...')
        print('Trying to fix input file format to a compatible CSV...')
        return _fix_csv(input_filename)
    else:
        return input_filename


def _fix_csv(input_filename):
    with open(input_filename, 'r') as file:
        fixed_lines = [line.replace(';', ',') for line in file.readlines()]
    fixed_filename = input_filename + '.fixed'
    with open(fixed_filename, 'w+') as fixed_file:
        fixed_file.writelines(fixed_lines)
    print('Fixed successfully into file {}'.format(fixed_filename))
    return fixed_filename
