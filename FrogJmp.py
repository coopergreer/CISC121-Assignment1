def solution(X, Y, D):
    # Start at the frog's initial position
    current_position = X
    jump_count = 0

    # Keep jumping until the frog reaches or passes the target
    while current_position < Y:
        current_position += D
        jump_count += 1

    # Return the total number of jumps
    return jump_count