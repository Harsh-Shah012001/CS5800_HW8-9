import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self):
        self.level = 0
        self.header = self.create_node(-1, self.level)

    def coin_flip(self):
        lvl = 0
        while random.randint(0, 1) == 1:
            lvl += 1
        return lvl

    def create_node(self, key, level):
        return Node(key, level)

    def insert_element(self, key):
        current = self.header
        update = [None] * (self.level + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if not current or current.key != key:
            rlevel = self.coin_flip()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update.append(self.header)
                self.header.forward.extend([None] * (rlevel - self.level))
                self.level = rlevel

            new_node = self.create_node(key, rlevel)

            for i in range(rlevel + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            print(f"Successfully Inserted key {key}")

    def delete_element(self, key):
        current = self.header
        update = [None] * (self.level + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

            print(f"Successfully deleted key {key}")

    def search_element(self, key):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            print(f"Found key: {key}")
        else:
            print(f"Key {key} not found")

    def display_list(self):
        print("\n*****Skip List*****")
        for i in range(self.level + 1):
            node = self.header.forward[i]
            print(f"Level {i}: ", end="")
            while node:
                print(node.key, end=" ")
                node = node.forward[i]
            print()

random.seed()
lst = SkipList()


lst.insert_element(3)
lst.insert_element(6)
lst.insert_element(7)
lst.insert_element(9)
lst.insert_element(12)
lst.insert_element(19)
lst.insert_element(17)
lst.insert_element(26)
lst.insert_element(21)
lst.insert_element(25)
lst.display_list()

lst.search_element(19)
lst.delete_element(19)
lst.display_list()

while(True):
    ch=input("Enter operation")
    if(ch=='1'):
        n=int(input("Enter element to insert: "))
        lst.insert_element(n)
    elif(ch=='2'):
        n=int(input("Enter element to delete: "))
        lst.delete_element(n)
    elif(ch=='3'):
        n=int(input("Enter element to search: "))
        lst.search_element(n)
    elif(ch=='4'):
        lst.display_list()
    elif(ch=='5'):
        print("Thank you")
        break