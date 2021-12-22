import argparse
import csv
from pathlib import Path


def default_key(elem):
    return elem


def get_rest(elem):
    return elem % 10


def merge(reverse, key, digit):
    src = "buffer.txt"
    seq1 = open("seq1.txt", 'r')
    seq2 = open('seq2.txt', 'r')
    dump = open(src, 'a')
    element1 = (seq1.readline().replace("\n", ''))
    element2 = (seq2.readline().replace("\n", ''))
    while True:
        if digit:
            if element1 != "":
                element1 = int(element1)
            if element2 != "":
                element2 = int(element2)
        if element1 != '' and element2 != '':
            if not reverse:
                if key(element1) <= key(element2):
                    dump.write(str(element1) + '\n')
                    element1 = seq1.readline().replace("\n", '')
                else:
                    dump.write(str(element2) + '\n')
                    element2 = seq2.readline().replace("\n", '')
            else:
                if key(element1) >= key(element2):
                    dump.write(str(element1) + '\n')
                    element1 = seq1.readline().replace("\n", '')
                else:
                    dump.write(str(element2) + '\n')
                    element2 = seq2.readline().replace("\n", '')
        else:
            if element1 == '' and element2 == '':
                break
            elif element1 != '' and element2 == '':
                dump.write(str(element1) + '\n')
                element1 = seq1.readline().replace("\n", '')
            elif element2 != '' and element1 == '':
                dump.write(str(element2) + '\n')
                element2 = seq2.readline().replace("\n", '')
    seq1.close()
    seq2.close()
    dump.close()
    open('seq1.txt', 'w').close()
    open('seq2.txt', 'w').close()


def is_digit(src):
    with open(src, 'r') as datafile:
        flag = True
        while flag:
            element = datafile.readline().replace('\n', '')
            if element != '':
                if '-' in element:
                    element = element.replace('-', '')
                    if not element.isdigit():
                        flag = False
                elif not element.isdigit():
                    flag = False
            else:
                break
        return flag


def read_csv(src, input_row):
    with open(src, newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        if not Path('data.txt').is_file():
            Path('data.txt').touch()
        open('data.txt', 'w').close()
        with open('data.txt', 'a') as txt_file:
            for row in reader:
                txt_file.write(row[input_row] + '\n')


def copy_from_to(from_file, to_file):
    open(to_file, 'w').close()
    from_file = open(from_file, 'r')
    to_file = open(to_file, 'a')
    while True:
        element1 = from_file.readline().replace("\n", '')
        if element1 == "":
            break
        to_file.write(element1 + "\n")
    from_file.close()
    to_file.close()


def sorted_check(src, reverse, key, digit):
    with open(src, 'r') as datafile:
        flag = True
        previous = ""
        while flag:
            element = datafile.readline().replace('\n', '')
            if digit and element != '':
                element = int(element)
            if element == '':
                break
            if not previous:
                previous = element
                continue
            if not reverse:
                if key(previous) > key(element):
                    flag = False
                    continue
            else:
                if key(previous) < key(element):
                    flag = False
                    continue
            previous = element
        return flag


def copy_csv_file(from_file, to_file):
    with open(from_file, newline='') as csv_source:
        with open(to_file, 'w', newline='') as csv_output:
            reader = csv.DictReader(csv_source, delimiter=';')
            writer = csv.DictWriter(csv_output, delimiter=';', fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)


def count_rows(src):
    with open(src, 'r', newline='') as csv_file:
        count = 0
        reader = csv.DictReader(csv_file, delimiter=';')
        for _ in reader:
            count += 1
    return count


def sort_row_in_csv(src, output, row):
    tmp_csv = 'tmp.csv'
    if not Path(tmp_csv).is_file():
        Path(tmp_csv).touch()
    copy_csv_file(src, tmp_csv)
    with open(tmp_csv, 'r', newline='') as tmp_data:
        reader = csv.DictReader(tmp_data, delimiter=';')
        fieldnames = reader.fieldnames
    with open(output, 'w', newline='') as csv_output:
        writer = csv.DictWriter(csv_output, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        count = count_rows(tmp_csv)
        with open('data.txt', 'r') as datafile:
            for i in range(count):
                element = datafile.readline().replace("\n", '')
                with open(tmp_csv, 'r', newline='') as tmp_data:
                    reader = csv.DictReader(tmp_data, delimiter=';')
                    for tmp_row in reader:
                        if tmp_row[row] == element:
                            writer.writerow(tmp_row)
                            break
    if Path(tmp_csv).is_file():
        Path(tmp_csv).unlink()



def separate_and_merge(src, reverse, key, digit):
    datafile = open(src, 'r')
    open('seq1.txt', 'w').close()
    open('seq2.txt', 'w').close()
    counter = 0
    previous = ""
    seq = list()
    seq.append(open('seq1.txt', 'a'))
    seq.append(open('seq2.txt', 'a'))
    flag = 0
    while True:
        element = datafile.readline().replace("\n", '')
        if digit and element:
            element = int(element)
        if not previous:
            previous = element
        if element == "":
            seq[0].close()
            seq[1].close()
            merge(reverse, key, digit)
            break
        if not reverse:
            if key(previous) > key(element):
                flag = 1 - flag
                counter += 1
        else:
            if key(previous) < key(element):
                flag = 1 - flag
                counter += 1
        previous = element
        if counter == 2:
            seq[0].close()
            seq[1].close()
            merge(reverse, key, digit)
            seq = list()
            seq.append(open('seq1.txt', 'a'))
            seq.append(open('seq2.txt', 'a'))
            counter = 0
        seq[flag].write(str(element) + "\n")
    seq[0].close()
    seq[1].close()
    datafile.close()


def natural_merge(src, output=None, reverse=False, key=default_key):
    file_format = src.split('.')[1]
    if key is None:
        key = default_key
    if output and output.split('.')[1] != file_format:
        raise TypeError('Different source and output extensions.')
    if file_format == "csv":
        row = input("Input a row to sort in csv file: ")
        read_csv(src, row)
        csv_source = src
        if output is None:
            output = src
        elif not Path(output).is_file():
            Path(output).touch()
        csv_output = output
        src = 'data.txt'
        output = 'data.txt'
    else:
        if output is None:
            output = src
        elif not Path(output).is_file():
            Path(output).touch()
            copy_from_to(src, output)
        else:
            copy_from_to(src, output)
    digit = is_digit(output)
    buffer = 'buffer.txt'
    while True:
        open(buffer, 'w').close()
        separate_and_merge(output, reverse, key, digit)
        copy_from_to(buffer, output)
        if sorted_check(output, reverse, key, digit):
            break
    if file_format == 'csv':
        sort_row_in_csv(csv_source, csv_output, row)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs='+', help="Файлы для внешней сортировки")
    parser.add_argument("-o", type=str, default=None, help='Файл для результатов')
    parser.add_argument("-r", action='store_true', help='Сортировка по убыванию')
    parser.add_argument("--key", type=str, default=None, help='Сортировка по ключу')
    arguments = parser.parse_args()
    parse_files = arguments.files
    parse_output = arguments.o
    parse_reverse = arguments.r
    parse_key = arguments.key
    if parse_key == 'get_rest':
        parse_key = get_rest
    else:
        parse_key = None
    if len(parse_files) > 1:
        parse_output = None
    continue_flag = True
    prev = ''
    for file in parse_files:
        extension = file.split('.')[1]
        if prev and extension != prev:
            continue_flag = False
        prev = extension
    for file in parse_files:
        if not Path(file).is_file():
            continue_flag = False
    if continue_flag:
        for source in parse_files:
            natural_merge(source, parse_output, parse_reverse, parse_key)
    else:
        print('Different file extensions or incorrect source file\n')
