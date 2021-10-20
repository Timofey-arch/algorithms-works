from LinkedList import LinkedList

def show_list(linked_list):
    iteration_item = linked_list.first_item
    for i in range(linked_list.length):
        print(iteration_item.data)
        iteration_item = iteration_item.next_link
    print("-------------------------------------")

def main():
    linked_list = LinkedList()
    linked_list.append_right(42)
    linked_list.append_right(43)
    linked_list.append_right(44)
    show_list(linked_list)


if __name__ == '__main__':
    main()
