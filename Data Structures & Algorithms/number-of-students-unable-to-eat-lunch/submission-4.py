# class Node:
#     def __init__(self, val, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev


# class ListNode:
#     def __init__(self, size):
#         self.head = Node(val)
#         self.size = 

#     def enqueue(self, val):
#         self.head.prev = Node(val, self.head)
#         self.head = self.head.prev

#     def dequeue(self, val, index):






class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #if front value on sandwiches does not exist in students array, size of array is number of students hungry

        size = len(students)
        hungry = size
        i, counter, tracker = 0, 0, 0
        while True:
            if students[i] == sandwiches[counter]:
                hungry -= 1
                counter += 1
                i += 1
                tracker = 0
            else:
                students.append(students[i])
                i += 1
                tracker += 1
            
            if tracker == size - counter:
                return hungry

            if hungry == 0:
                return hungry








