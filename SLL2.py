class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
#first_node = Node(21)
#print(f"first node - {first_node}")
#print(f"first node - {first_node.value}")

class SLL:
    def __init__(self, head = None):
        self.head = head

    def addToBack(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def display(self):
        str_node = ""
        node_num = 1
        runner = self.head
        while runner: #same as while runner != None

            str_node += f"the value of {node_num} node is {runner.value}"
            node_num += 1
            runner = runner.next
        print(str_node)
        return self

    def length(self):
        node_num = 0
        runner = self.head
        while runner: #same as while runner != None
            node_num += 1
            runner = runner.next
        print(node_num)
        return self

    def contain(self, value):
        runner = self.head
        while runner:
            if value == runner.value:
                return True
            return False
        return self

first_sll = SLL(Node(21))
first_sll.addToBack(51).addToBack(71).addToBack(7).addToBack(45)
#print(first_sll.head.next.value)




first_sll.display()
first_sll.length()
first_sll.contain(71)