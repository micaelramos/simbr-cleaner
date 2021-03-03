import csv
import json
from parameters import fields_to_pop, fields_to_format_date, fields_to_int, fields_to_rename
from datetime import datetime


def clean_data(filename):
    d = _csv_to_dict(filename)
    only_non_fetal = _filter_by_kv(d, "TIPOBITO", "2")
    clean_data = _pop_fields(only_non_fetal, fields_to_pop)
    clean_data = _rename_fields(clean_data, fields_to_rename)
    clean_data = _change_to_int(clean_data, fields_to_int)
    clean_data = _format_date(clean_data, fields_to_format_date)
    return clean_data


def _csv_to_dict(filename):
    with open(filename, 'r') as data:
        return [i for i in csv.DictReader(data)]


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


def _map(data, mapping):



if __name__ == '__main__':
    data = clean_data('2019.csv')
    with open('cleaned_2019.json', 'w') as file:
        json.dump(data, file)
