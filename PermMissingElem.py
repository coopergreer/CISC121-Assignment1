def solution(A):
    # Find how many elements are currently in the array
    N = len(A)

    # Check every expected number from 1 through N + 1
    for number in range(1, N + 2):
        if number not in A:
            return number