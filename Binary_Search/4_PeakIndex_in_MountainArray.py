'''
Approach:- Binary Search
Array itself hass two parts that is increasing and decreasing

everytime you check if mid is greater than mid+1;
    if it is grreater than mid+1 then you are in second part of array and mid might be the answer or answer lies in left side so   end = mid
    
    if it is not greater than mid+1 then search you are in first part of array and search space is on right side and definately mid is not your answer so start = mid + 1
    
    Exit Conditon: when start == mid then break the loop and return start/end 

'''

def peakElementInMountainArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + (end - start) // 2)
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start

print(peakElementInMountainArray([1,2,3,4,6,19,4,3,2,1]))