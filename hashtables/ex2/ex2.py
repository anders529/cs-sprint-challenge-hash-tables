#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    route = [None] * length
    flights = {}
    for i in tickets:
        if i.source == 'NONE':
            first_flight = i
        flights[i.source] = i.destination
    route[0] = first_flight.destination
    for i in range(1, length):
        source = route[i - 1]
        route[i] = flights[source]
    return route
