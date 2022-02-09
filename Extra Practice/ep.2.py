"""
Problem statement:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LL:
    tail = None

    def add(self, data):
        node = Node(data, self.tail)
        self.tail = node

    def convert_to_num(self):
        num_str = ""
        node = self.tail
        while node != None:
            num_str = str(node.data) + num_str
            node = node.next
        return int(num_str)

    def print(self):
        node = self.tail
        ret_str = ""
        while node != None:
            ret_str += str(node.data) + "->"
            node = node.next
        print(ret_str[:-2])


def Add_Two_Nums(ll1, ll2):
    num1 = ll1.convert_to_num()
    num2 = ll2.convert_to_num()
    num3 = num1 + num2
    num3_str = str(num3)
    ll3 = LL()
    for c in num3_str:
        ll3.add(int(c))
    return ll3


# //***************************************************************************************//
# //
# //


def main():
    ll1 = LL()
    ll1.add(3)
    ll1.add(4)
    ll1.add(2)

    ll2 = LL()
    ll2.add(4)
    ll2.add(6)
    ll2.add(5)

    ll3 = Add_Two_Nums(ll1, ll2)
    ll3.print()


if __name__ == "__main__":
    main()
