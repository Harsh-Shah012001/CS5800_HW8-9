class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.sibling = None
        self.child = None

    def reverse(self, sibl):
        ret = self
        if self.sibling:
            ret = self.sibling.reverse(self)
        self.sibling = sibl
        return ret

    def find_min_node(self):
        x = self
        y = self
        min_key = self.key
        while x is not None:
            if x.key < min_key:
                y = x
                min_key = x.key
            x = x.sibling
        return y

    def find_node_with_key(self, value):
        temp = self
        node = None
        while temp is not None:
            if temp.key == value:
                node = temp
                break
            if temp.child is not None:
                node = temp.child.find_node_with_key(value)
                if node is not None:
                    break
            temp = temp.sibling
        return node

    def get_size(self):
        size = 1
        if self.child is not None:
            size += self.child.get_size()
        if self.sibling is not None:
            size += self.sibling.get_size()
        return size

class BinomialHeap:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size

    def make_empty(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        if value > 0:
            temp = BinomialHeapNode(value)
            if self.head is None:
                self.head = temp
                self.size = 1
            else:
                self.union_nodes(temp)
                self.size += 1

    def merge(self, bin_heap):
        temp1 = self.head
        temp2 = bin_heap

        if temp1 is None:
            self.head = temp2
            return
        if temp2 is None:
            return

        if temp1.degree <= temp2.degree:
            self.head = temp1
        else:
            self.head = temp2
            temp2 = temp1
            temp1 = self.head

        while temp1.sibling is not None and temp2 is not None:
            if temp1.sibling.degree <= temp2.degree:
                temp1 = temp1.sibling
            else:
                temp3 = temp1.sibling
                temp1.sibling = temp2
                temp2 = temp3

        if temp1.sibling is None:
            temp1.sibling = temp2

    def union_nodes(self, bin_heap):
        self.merge(bin_heap)
        prev_temp = None
        temp = self.head
        next_temp = self.head.sibling

        while next_temp is not None:
            if temp.degree != next_temp.degree or (next_temp.sibling is not None and next_temp.sibling.degree == temp.degree):
                prev_temp = temp
                temp = next_temp
            else:
                if temp.key <= next_temp.key:
                    temp.sibling = next_temp.sibling
                    next_temp.parent = temp
                    next_temp.sibling = temp.child
                    temp.child = next_temp
                    temp.degree += 1
                else:
                    if prev_temp is None:
                        self.head = next_temp
                    else:
                        prev_temp.sibling = next_temp
                    temp.parent = next_temp
                    temp.sibling = next_temp.child
                    next_temp.child = temp
                    next_temp.degree += 1
                    temp = next_temp
            next_temp = temp.sibling

    def find_minimum(self):
        if self.head is None:
            return None
        return self.head.find_min_node().key

    def delete(self, value):
        if self.head is not None and self.head.find_node_with_key(value) is not None:
            self.decrease_key(value, self.find_minimum() - 1)
            self.extract_min()

    def decrease_key(self, old_value, new_value):
        node = self.head.find_node_with_key(old_value)
        if node is None:
            return
        node.key = new_value
        temp = node
        temp_parent = node.parent

        while temp_parent is not None and temp.key < temp_parent.key:
            temp.key, temp_parent.key = temp_parent.key, temp.key
            temp = temp_parent
            temp_parent = temp_parent.parent

    def extract_min(self):
        if self.head is None:
            return -1

        temp = self.head
        prev_temp = None
        min_node = self.head.find_min_node()

        while temp.key != min_node.key:
            prev_temp = temp
            temp = temp.sibling

        if prev_temp is None:
            self.head = temp.sibling
        else:
            prev_temp.sibling = temp.sibling

        temp = temp.child
        fake_node = temp

        while temp is not None:
            temp.parent = None
            temp = temp.sibling

        if self.head is None and fake_node is None:
            self.size = 0
        elif self.head is None:
            self.head = fake_node.reverse(None)
            self.size = self.head.get_size()
        elif fake_node is None:
            self.size = self.head.get_size()
        else:
            self.union_nodes(fake_node.reverse(None))
            self.size = self.head.get_size()

        return min_node.key

    def display_heap(self):
        if self.head is None:
            print("\nHeap is empty.")
            return
        print("\nHeap:")
        self.display_heap_helper(self.head)

    def display_heap_helper(self, node):
        if node is not None:
            print(f"Key: {node.key}, Degree: {node.degree}, ", end="")
            if node.parent:
                print(f"Parent: {node.parent.key}, ", end="")
            else:
                print("Parent: None, ", end="")
            if node.sibling:
                print(f"Sibling: {node.sibling.key}, ", end="")
            else:
                print("Sibling: None, ", end="")
            if node.child:
                print(f"Child: {node.child.key}")
            else:
                print("Child: None")
            if node.child:
                self.display_heap_helper(node.child)
            if node.sibling:
                self.display_heap_helper(node.sibling)

def main():
    # Make object of BinomialHeap
    bin_heap = BinomialHeap()

    # Inserting in the binomial heap
    # Custom input integer values
    bin_heap.insert(12)
    bin_heap.insert(8)
    bin_heap.insert(5)
    bin_heap.insert(15)
    bin_heap.insert(7)
    bin_heap.insert(2)
    bin_heap.insert(9)

    # Size of binomial heap
    # print("Size of the binomial heap is", bin_heap.get_size())

    # # Displaying the binomial heap
    # bin_heap.display_heap()

    # # Deletion in binomial heap
    # bin_heap.delete(15)
    # bin_heap.delete(8)

    # # Size of binomial heap
    # print("Size of the binomial heap is", bin_heap.get_size())

    # # Displaying the binomial heap
    # bin_heap.display_heap()

    # # Making the heap empty
    # bin_heap.make_empty()

    # # checking if heap is empty
    # print(bin_heap.is_empty())

    bin_heap2=BinomialHeap()
    bin_heap2.insert(120)
    bin_heap2.insert(28)
    
    bin_heap.union_nodes(bin_heap2.head)
    print("After Union: ")
    bin_heap.display_heap()

    bin_heap.decrease_key(120,1)
    print("After Decrease Key: ")
    bin_heap.display_heap()
    
    bin_heap.extract_min()
    bin_heap.display_heap()
if __name__ == "__main__":
    main()
