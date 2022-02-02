"""
Problem statement:
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based on arrival time)
of all animals at the shelter, or they can select wheather they would prefer a dog
or a cat (and will receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structures to maintain this system and
implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may
use the built-in LinkedList data structure.
"""

import enum

# //----------------------------------------------------------------------------------//
# //
# //

class Animal(enum.Enum):
    dog = 1
    cat = 2

class Node:
    def __init__(self,animal,number,next=None):
        self.animal = animal
        self.number = number
        self.next = next

class Queue:

    head = None
    tail = None
    count = 0

    def enqueue(self,animal):
        self.count += 1

        new_tail = Node(animal,self.count)
        
        if self.tail:
            self.tail.next = new_tail
        
        self.tail = new_tail

        if not self.head:
            self.head = self.tail

    def dequeue_any(self):
        animal = str(self.head.animal.name) + str(self.head.number)
        self.head = self.head.next
        return animal

    def dequeue(self,dequeue_type):
        
        if self.head.animal == dequeue_type:
            animal = str(self.head.animal.name) + str(self.head.number)
            self.head = self.head.next
            return animal

        node = self.head
        while node != None:
            next_node = node.next
            if next_node.animal == dequeue_type:
                animal = str(next_node.animal.name) + str(next_node.number)
                node.next = next_node.next
                return animal
            node = node.next

        return f"No {dequeue_type.name} available."

    def dequeue_dog(self):
        return self.dequeue(Animal.dog)

    def dequeue_cat(self):
        return self.dequeue(Animal.cat)


    def print(self):
        print("Queue:")
        node = self.head
        while node != None:
            animal = str(node.animal.name) + str(node.number)
            print(animal)
            node = node.next

        

# //----------------------------------------------------------------------------------//
# //
# //


def main():
    q = Queue()
    q.enqueue(Animal.dog)
    q.enqueue(Animal.dog)
    q.print()
    print(f"Congrats on adopting {q.dequeue_dog()}!")
    q.enqueue(Animal.cat)
    q.enqueue(Animal.dog)
    q.enqueue(Animal.cat)
    q.print()
    print(f"Congrats on adopting {q.dequeue_cat()}!")
    q.print()
    print(f"Congrats on adopting {q.dequeue_any()}!")
    q.print()


if __name__ == "__main__":
    main()
