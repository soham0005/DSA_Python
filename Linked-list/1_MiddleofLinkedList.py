# Leetcode - 876 Middle of Linked List
'''
Approach: Naive Approach is to use a counter which counts the element and divide by 3 and use again a loop to reach to the half

Optimum Approach:- Use Fast and slow pointers:


   
        count = 0
        curr = head
        while(curr is not None):
            count +=1
            curr = curr.next
        count = count / 2

        temp = head
        ans = 0
        while(ans < count):
            temp = temp.next
            ans += 1
        return temp
    
        Optimized Solution
        if (head is None or head.next is None):
            return head
        elif (head.next.next is None):
            return head.next
        else:
            slow = head
            fast = head.next

            while(fast is not None):
                fast = fast.next
                if (fast is not None):
                    fast = fast.next
                slow = slow.next
            return slow

        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
'''