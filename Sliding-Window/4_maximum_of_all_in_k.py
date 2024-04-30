from collections import deque

def max_in_window(arr, k):
    n = len(arr)
    result = []
    window = deque()

    for i in range(n):
        # Remove elements out of the window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements smaller than the current element
        while window and arr[window[-1]] < arr[i]:
            window.pop()

        window.append(i)

        # Once the window size is reached, start appending maximum element
        if i >= k - 1:
            result.append(arr[window[0]])

    return result

# Example usage:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("Maximum element in each window of size", k, ":", max_in_window(arr, k))
