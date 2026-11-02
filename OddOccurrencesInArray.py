def solution(A):
    # Check each number in the array
    for number in A:

        # Count how many times the number appears
        count = A.count(number)

        # Return the number if it appears an odd number of times
        if count % 2 == 1:
            return number