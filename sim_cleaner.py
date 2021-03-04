import json
import argparse
from parameters import fields_to_pop, fields_to_format_date, fields_to_int, fields_to_rename
from file_reader import read_file
from datetime import datetime


def clean_data(input_filename):
    d = read_file(input_filename)
    only_non_fetal = _filter_by_kv(d, "TIPOBITO", "2")
    # TODO: consider currying for cleanining functions...
    clean_data = _pop_fields(only_non_fetal, fields_to_pop)
    clean_data = _change_to_int(clean_data, fields_to_int)
    clean_data = _format_date(clean_data, fields_to_format_date)
    clean_data = _rename_fields(clean_data, fields_to_rename)
    return clean_data


def _filter_by_kv(data, k, v):
    return [i for i in data if i[k] == v]


def _pop_fields(data, fields):
    for item in data:
        [item.pop(k) for k in fields]
    return data


def _rename_fields(data, fields):
    for item in data:
        for field in fields:
            item[field['new']] = item.pop(field['old'])
    return data


def _change_to_int(data, fields):
    for item in data:
        for field in fields:
            if item[field]:
                item[field] = int(item[field])
    return data


def _format_date(data, fields):
    for item in data:
        for field in fields:
            if item[field]:
                year = item[field][-4:]
                month = item[field][-6:][:2]
                day = item[field].split(month + year)[0]
                date = datetime(int(year), int(month), int(day))
                item[field] = date.isoformat()
    return data


def save_results(filename, result_data):
    with open(filename, 'w+') as file:
        json.dump(result_data, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SIM Data Cleaner.')
    parser.add_argument('-i', dest='input', help='Input file path (CSV format)')
    parser.add_argument('-o', dest='output', help='Output file path (JSON format)')
    args = parser.parse_args()
    data = clean_data(args.input)
    save_results(args.output, data)
    print('Successfully cleaned {} record(s) to file: {}'.format(len(data), args.output))
