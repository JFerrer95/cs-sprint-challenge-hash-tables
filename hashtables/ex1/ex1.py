def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    storage = {}
    for i in range(length):
        otherWeight = limit - weights[i]
        if otherWeight in storage:
            otherIndex = storage[otherWeight]
            return (i, otherIndex)
        else:
            storage[weights[i]] = i
    return None

