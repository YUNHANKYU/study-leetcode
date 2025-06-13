# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First Try
# Time Complexity: O(n)
# Space Complexity: O(n)
# idea
# : use a list to store the nodes
# : if the next node is in the list, there is a cycle


def hasCycleFirst(head: [ListNode]) -> bool:
    if head == None:
        return False
    nodeList = [head]
    nextNode = head.next

    while nextNode != None:
        if nextNode in nodeList:
            return True
        else:
            nodeList.append(nextNode)
            nextNode = nextNode.next

    return False


# Floyd's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# idea
# : use two pointers, slow and fast
# : slow moves one step at a time
# : fast moves two steps at a time
# : if there is a cycle, they will meet at some point
# : if the fast reaches the end, there is no cycle
def hasCycleFloyd(head: [ListNode]) -> bool:
    if head == None:
        return False
    slow = head
    fast = head
    has_cycle = False
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return False

    slow = head
    count = 0
    while slow != fast:
        print('slow_value: {}, fast_value: {}'.format(slow.val, fast.val))
        slow = slow.next
        fast = fast.next
        count += 1
    print(count)
    return True


node4 = ListNode(-4)
node3 = ListNode(0)
node2 = ListNode(2)
node1 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(hasCycleFloyd(node1))
