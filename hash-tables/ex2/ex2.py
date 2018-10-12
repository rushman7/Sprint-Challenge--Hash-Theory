def reconstruct_trip(tickets):
    flights = {}
    planned_trip = []
    for ticket in tickets:
        flights[ticket[0]] = ticket[1] # setting the first ticket to be the second ticket when switching
    active_ticket = flights[None] # default active ticket
    while active_ticket != None:
        planned_trip.append(active_ticket) # adding ticket to trip
        if active_ticket not in flights: # no ticket returns empty array
            return []
        active_ticket = flights[active_ticket]
    return planned_trip

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
