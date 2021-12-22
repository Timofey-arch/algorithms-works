import argparse


class FileArray:
    def __init__(self, src):
        self.src = src
        self.length = self.count_len()

    def count_len(self):
        length = 0
        flag = True
        with open(self.src, 'r') as data:
            while flag:
                element = data.readline().replace('\n', '')
                if element != "":
                    length += 1
                else:
                    flag = False
        return length

    def append(self, item):
        source = open(self.src, 'a')
        source.writelines(item + '\n')
        source.close()
        self.length += 1

    def separate_sequence(self, additional_sequence, first_sequence, second_sequence, reverse):
        count_of_separators = 0
        for i in range(self.length - 1):
            if not reverse:
                if self[i] < self[i + 1]:
                    additional_sequence.append(self[i])
                else:
                    additional_sequence.append(self[i])
                    additional_sequence.append('_')
                    count_of_separators += 1
            else:
                if self[i] > self[i + 1]:
                    additional_sequence.append(self[i])
                else:
                    additional_sequence.append(self[i])
                    additional_sequence.append('_')
                    count_of_separators += 1
        additional_sequence.append(self[self.length - 1])
        additional_sequence.append('_')
        count_of_separators += 1

        sequences = [first_sequence, second_sequence]
        flag = additional_sequence.length
        i = 0
        j = 0
        while flag:
            while additional_sequence[i] != '_':
                sequences[j].append(additional_sequence[i])
                i += 1
                flag -= 1
            i += 1
            j += 1
            flag -= 1
            if j == 2:
                j = 0
        additional_sequence.clear()

    def check_for_sort(self):
        for i in range(self.length - 1):
            if self[i] > self[i + 1]:
                return False
        return True

    def check_for_reverse_sort(self):
        for i in range(self.length - 1):
            if self[i] <= self[i + 1]:
                return False
        return True

    def clear(self):
        source = open(self.src, 'w')
        self.length = 0
        source.close()

    def copy(self, copy_to):
        with open(self.src) as first, open(copy_to.src, 'w') as second:
            data = first.read()
            second.write(data)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        iteration_index = 0
        with open(self.src) as data:
            for i in range(self.length):
                element = data.readline().replace('\n', '')
                if iteration_index == index:
                    return element
                else:
                    iteration_index += 1
            raise IndexError("Неверный индекс")


def merge_sort(first_sequence, second_sequence, new_sequence, key, reverse):
    a = 0
    b = 0
    while a < len(first_sequence) and b < len(second_sequence):
        if not reverse:
            if key(int(first_sequence[a])) < key(int(second_sequence[b])):
                new_sequence.append(first_sequence[a])
                a += 1
            elif key(int(first_sequence[a])) > key(int(second_sequence[b])):
                new_sequence.append(second_sequence[b])
                b += 1
            else:
                new_sequence.append(first_sequence[a]), new_sequence.append(second_sequence[b])
                a, b = a + 1, b + 1
        else:
            if key(int(first_sequence[a])) > key(int(second_sequence[b])):
                new_sequence.append(first_sequence[a])
                a += 1
            elif key(int(first_sequence[a])) < key(int(second_sequence[b])):
                new_sequence.append(second_sequence[b])
                b += 1
            else:
                new_sequence.append(first_sequence[a]), new_sequence.append(second_sequence[b])
                a, b = a + 1, b + 1
    while a < len(first_sequence):
        new_sequence.append(first_sequence[a])
        a = a + 1
    while b < len(second_sequence):
        new_sequence.append(second_sequence[b])
        b = b + 1
    first_sequence.clear()
    second_sequence.clear()
    return new_sequence


def native_sort(src, reverse, key, output):
    flag = True
    source_sequence = FileArray(src)
    first_sequence = FileArray("first_sequence.txt")
    second_sequence = FileArray("second_sequence.txt")
    new_sequence = FileArray("new_file.txt")
    output_file = FileArray("output.txt")
    if source_sequence.length == 0:
        return print("File is empty.")
    if source_sequence.length == 1:
        return print("File has only one element. That is stupid.")
    if not reverse:
        if source_sequence.check_for_sort():
            return
    else:
        if source_sequence.check_for_reverse_sort():
            return
    if output:
        output_file.clear()
        source_sequence.copy(output_file)
    while flag:
        if not reverse:
            source_sequence.separate_sequence(new_sequence, first_sequence, second_sequence, reverse)
            new_sequence = merge_sort(first_sequence, second_sequence, new_sequence, key, reverse)
            if new_sequence.check_for_sort():
                flag = False
            new_sequence.copy(source_sequence)
            new_sequence.clear()
        else:
            source_sequence.separate_sequence(new_sequence, first_sequence, second_sequence, reverse)
            new_sequence = merge_sort(first_sequence, second_sequence, new_sequence, key, reverse)
            if new_sequence.check_for_reverse_sort():
                flag = False
            new_sequence.copy(source_sequence)
            new_sequence.clear()


def my_sort(src, reverse=False, key=None, output=None):
    key = key if key is not None else lambda x: x
    native_sort(src, reverse, key, output)


# my_sort("s.txt")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Файл для внешней сортировки")
    parser.add_argument("-output", type=str, default=None, help='Файл для результатов')
    parser.add_argument("-reverse", help='Сортировка по убыванию', default=False)
    parser.add_argument("-key", type=str, default=None, help='Сортировка по ключу')
    args = parser.parse_args()
    my_sort(str(args.file), reverse=args.reverse, key=args.key, output=args.output)
