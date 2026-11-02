def solution(A, K):
    # Return the array immediately if it is empty
    if len(A) == 0:
        return A

    # Rotate the array to the right K times
    for i in range(K):
        last = A.pop()
        A.insert(0, last)

    # Return the rotated array
    return A