"""
This script attempts the simulate the following problem (taken from: http://fivethirtyeight.com/features/will-someone-be-sitting-in-your-seat-on-the-plane/)
There’s an airplane with 100 seats, and there are 100 ticketed passengers each with an assigned seat. They line up to board in some random order. However, the first person to board is the worst person alive, and just sits in a random seat, without even looking at his boarding pass. Each subsequent passenger sits in his or her own assigned seat if it’s empty, but sits in a random open seat if the assigned seat is occupied. What is the probability that you, the hundredth passenger to board, finds your seat unoccupied?
"""
"""
Solution (mine):
In all cases it boils down to two scenarios:

    the asshole sits in your seat or his seat (50% chance of success: guaranteed failure if he sits in your seat, guaranteed success if he sits in his seat)
    the asshole sits in someone else's seat (neither yours nor his) leaving his seat vacant, and the problem reduces to an identical scenario on a smaller plane.
"""

import random

def all_aboard(number_of_seats):
    """
    Run a random simulation of the described scenario on a plane with number_of_seats seats.
    Return True if your (the final passenger to board) seat is occupied by someone else, False otherwise
    """
    
    #create a plane with number_of_seats vacant seats, labeled 0,1,..,number_of_seats-1
    seats = dict() # seat number -> bool describing whether seat is occupied (True) or vacant (False)
    for i in range(number_of_seats): #mark each seat..
        seats[i] = False #..as vacant
    
    #without loss of generality, assume that the asshole who boards first has the ticket for seat 0,
    #the passenger who boards next has the ticket for seat 1,
    #the passenger who boards after that has the ticket for seat 2, etc..
    #and you have the ticket for seat number_of_seats-1
    your_seat_number = number_of_seats-1
    
    #asshole (first passenger to board) occupies a random seat
    i = random.randint(0,number_of_seats-1) #choose a random seat
    seats[i] = True #..mark random seat as occupied and continue boarding the plane
    
    #all remaining passengers except you (the final passenger) board the plane
    #(according to the prescribed rules)
    for i in range(1,number_of_seats-1): #the passenger with the ticket for seat i boards the plane
        if seats[i]: #if seat i is occupied..
            j = random.choice(tuple(i for i in seats if not seats[i])) #..then this passenger chooses a different seat to occupy
            seats[j] = True #..mark seat j as occupied
        else: #otherwise the passenger sits in his assigned seat..
            seats[i] = True #..and we mark seat i as occupied
    
    #now that everyone except you (the final passenger) have boarded the plane..
    return seats[your_seat_number] #..return whether your seat is occupied or vacant
    

def monte_carlo(number_of_seats,number_of_simulations):
    """
    Run a random simulation of the described scenario multiple times,
    returning the number of times that your (the final passenger) seat is left vacant.
    
    number_of_seats -- the number of seats on the plane
    number_of_iterations -- the number of times to simulate the scenario
    """
    counter = 0 #counts the number of times that your seat is left vacant
    for i in range(number_of_simulations):
        if all_aboard(number_of_seats):
          counter += 1
    return counter
  
def more_efficient(number_of_seats):
    """
    This is a slightly more efficient implementation of all_aboard,
    that terminates the simulation as soon as your (the final passenger)
    seat is occupied.
    """
    
    #create a plane with number_of_seats vacant seats, labeled 0,1,..,number_of_seats-1
    seats = dict() # seat number -> bool describing whether seat is occupied (True) or vacant (False)
    for i in range(number_of_seats): #mark each seat..
        seats[i] = False #..as vacant
    
    #without loss of generality, assume that the asshole who boards first has the ticket for seat 0,
    #the passenger who boards next has the ticket for seat 1,
    #the passenger who boards after that has the ticket for seat 2, etc..
    #and you have the ticket for seat number_of_seats-1
    your_seat_number = number_of_seats-1
    
    #asshole (first passenger to board) occupies a random seat
    i = random.randint(0,number_of_seats-1) #choose a random seat
    if i == your_seat_number: #if the asshole takes your seat..
        return False #..then we already know that your seat will not be vacant and can terminate the simulation
    else: #otherwise..
        seats[i] = True #..mark random seat as occupied and continue boarding the plane
    
    #all remaining passengers except you (the final passenger) board the plane
    #(according to the prescribed rules)
    for i in range(1,number_of_seats-1): #the passenger with the ticket for seat i boards the plane
        if seats[i]: #if seat i is occupied..
            j = random.choice(tuple(i for i in seats if not seats[i])) #..then this passenger chooses a different seat to occupy
            if j==your_seat_number: #if this passenger chooses to sit in your seat..
                return False #then we already know that your seat will not be vacant and can terminate the simulation
            else: #otherwise..
                seats[j] = True #..mark seat j as occupied
        else: #otherwise the passenger sits in his assigned seat..
          seats[i] = True #.. and we mark seat i as occupied
    
    return True #you (the final passenger) are the only person left to board, and no one has taken your seat
