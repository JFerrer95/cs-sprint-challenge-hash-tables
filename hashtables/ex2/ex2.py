#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    storage = {}
    route = [None] * length
    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        storage[tickets[i].source] = tickets[i].destination

    for i in range(length):
        if route[i - 1] != None:
            route[i] = storage[route[i - 1]]
    return route

tickets = [Ticket("NONE", "JFK"), Ticket("MCO", "PIT"), Ticket("JFK", "MCO"), Ticket("PIT", "NONE")] 


print(reconstruct_trip(tickets, 4))