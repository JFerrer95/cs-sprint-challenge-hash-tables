def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    storage = {}

    for num in a:
        if -num in storage:
            result.append(abs(num))
        else:
            storage[num] = num
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
