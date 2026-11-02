def solution(A):
    # Find the number of elements in the array
    N = len(A)

    # Check that every number from 1 to N appears exactly once
    for number in range(1, N + 1):
        if A.count(number) != 1:
            return 0

    # Return 1 if the array is a valid permutation
    return 1