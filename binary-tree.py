print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    name = ["J", "I", "M", "W", "E", "L", "L", "L",
            "M", "A", "N", "G", "U", "L", "A", "B", "N", "A", "N"]
    numbers = [32, 22, 24, 6, 69, 22, 54, 24, 69, 19, 75, 10, 32]

name_tree = build_tree(name)
print("\t\t\t", "-"*30)
print("\t\t\t====BINARY TREE FOR LETTERS OF NAME====")
print("Letters of my full name:", name)
print("\nMinimum value:", name_tree.find_min())
print("Maximum value:", name_tree.find_max())
print("Is the letter U included in the list?:", name_tree.search("U"))
print("Is the letter S included in the list?:", name_tree.search("S"))

name_tree.delete("N")
print("After deleting letter N, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())
name_tree.delete("A")
print("After deleting letter A, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())
name_tree.delete("L")
print("After deleting letter L, The current list of letters was now being shown in order traversal:\n",
      name_tree.in_order_traversal())

print("\nIn order traversal of the list:", name_tree.in_order_traversal())
print("Pre order traversal of the list:", name_tree.pre_order_traversal())
print("Post order traversal of the list:", name_tree.post_order_traversal())


numbers_tree = build_tree(numbers)
print('\n')
print("\t\t\t", "-"*24)
print("\t\t\t====BINARY TREE FOR NUMBERS====")
print("Some random numbers:\n", numbers)
print("\nMinimum value:", numbers_tree.find_min())
print("Maximum value:", numbers_tree.find_max())
print("Is the number 1 included in the list?:", numbers_tree.search(1))
print("Is the number 69 included in the list?:", numbers_tree.search(69))

numbers_tree.delete(24)
print("After deleting number 24, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())
numbers_tree.delete(75)
print("After deleting number 75, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())
numbers_tree.delete(32)
print("After deleting number 32, The current list for numbers was now being shown in order traversal:\n",
      numbers_tree.in_order_traversal())

print("\nSum of all numbers:", numbers_tree.calculate_sum())

print("In order traversal of the list:", numbers_tree.in_order_traversal())
print("Pre order traversal of the list:",
      numbers_tree.pre_order_traversal())
print("Post order traversal of the list:",
      numbers_tree.post_order_traversal())