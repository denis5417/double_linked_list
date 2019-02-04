class DoubleLinkedList():
    class Node():
        def __init__(self, value, next, prev):
            self.value = value
            self.next = next
            self.prev = prev


    def append(self, value):
        if self.__head is None:
            self.__head = self.__tail = self.Node(value, None, None)
        else:
            temp = self.__tail
            temp.next = self.Node(value, None, temp)
            self.__tail = temp.next
        self.__lenght += 1


    def extend(self, iterable):
        for i in iterable:
            self.append(i)


    def __init__(self, iterable=None):
        self.__head = None
        self.__tail = None
        self.__lenght = 0
        if iterable:
            self.extend(iterable)
    

    def __insert_first(self, value):
        if self.__head is None:
            self.__head = self.__tail = self.Node(value, None, None)
        else:
            temp = self.__head
            temp.prev = self.Node(value, temp, None)
            self.__head = temp.prev
    

    def __iter(self, reverse=False, start_node=None):
        if not self.__lenght:
            return None 
        if not start_node:
            cur_node = self.__tail if reverse else self.__head
        else:
            cur_node = start_node
        yield cur_node
        for i in range(self.__lenght - 1):
            cur_node = cur_node.prev if reverse else cur_node.next
            yield cur_node


    def __iter_value(self, reverse=False):
        for node in self.__iter(reverse):
            yield node.value 


    def __get_node(self, key):
        if key < 0:
            key += self.__lenght
        if key >= self.__lenght or key < 0:
            raise KeyError('DoubleLinkedList key out of range error')
        if key > self.__lenght // 2:
            counter = self.__lenght - 1
            for node in self.__iter(reverse=True):
                if counter == key:
                    return node
                counter -= 1
        else:
            counter = 0
            for node in self.__iter():
                if counter == key:
                    return node
                counter += 1


    def insert(self, key, value):
        if key >= self.__lenght:
            self.append(value)
            return
        if key == 0:
            self.__insert_first(value)
        else:
            temp = self.__get_node(key - 1)
            temp_next = temp.next
            temp.next = self.Node(value, temp_next, temp)
            temp_next.prev = temp.next
        self.__lenght += 1


    def __len__(self):
        return self.__lenght


    def __getitem__(self, key):
        return self.__get_node(key).value


    def __setitem__(self, key, value):
        self.__get_node(key).value = value


    def __get_node_by_item(self, item):
        for i, node in enumerate(self.__iter()):
            if node.value == item:
                return i, node
        raise ValueError('{} is not in DoubleLinkedList'.format(item))


    def index(self, item):
        return self.__get_node_by_item(item)[0]


    def count(self, item):
        counter = 0
        for value in self.__iter_value():
            if value == item:
                counter += 1
        return counter


    def __delnode(self, node):
        if node != self.__head:
            node.prev.next = node.next
        else:
            self.__head = node.next
        if node != self.__tail:
            node.next.prev = node.prev
        else:
            self.__tail = node.prev
        self.__lenght -= 1


    def remove(self, item):
        self.__delnode(self.__get_node_by_item(item)[1])


    def pop(self, index=0):
        node = self.__get_node(index)
        self.__delnode(node)
        return node.value


    def clear(self):
        self.__init__()


    def reverse(self):
        for node in self.__iter(reverse=True, start_node=self.__head):
            node.prev, node.next = node.next, node.prev
        self.__head, self.__tail = self.__tail, self.__head


    def __delitem__(self, key):
        self.__delnode(self.__get_node(key))


    def __iter__(self):
        return self.__iter_value()


    def __reversed__(self):
        return self.__iter_value(reverse=True)


    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False


    def __str__(self):
        return '[{}]'.format(', '.join(str(value) for value in self.__iter_value()))


    def __repr__(self):
        return self.__str__()


    def sort(self, key=None):
        self.__init__(sorted(self, key=key))
