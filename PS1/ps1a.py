###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from fileinput import filename

from numpy import empty
from ps1_partition import get_partitions
from time import time
import pandas as pd
import numpy as np

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    df = pd.read_csv(filename, names=["Cows", "Weight"], header=None)
    cows = list(df["Cows"])
    weight = list(df["Weight"])

    cows_dict = {key:value for key,value in zip(cows, weight)}

    return cows_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_sorted = {key: value for key, value in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    trips = list()

    while cows_sorted:
        total_weight = 0
        trip = list()
        for cow, weight in list(cows_sorted.items()):
            if weight > limit:
                del cows_sorted[cow]
            elif (weight + total_weight) <= limit:
                trip.append(cow)
                total_weight += weight 
                del cows_sorted[cow]
        trips.append(trip)
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    potential_trips_combinations = list(get_partitions(cows.keys()))

    valid_trips_solutions = list()

    for potential_solution_trips in potential_trips_combinations:
        trips_weights = dict()
        for trip in potential_solution_trips:
            total_weight = 0
            for cow in trip:
                total_weight += cows[cow]
            trips_weights[tuple(trip)] = total_weight
        if all(weight <= limit for weight in trips_weights.values()):
            valid_trips_solutions.append(list(trips_weights.keys()))

    min_solution = len(min(valid_trips_solutions, key=len))
    best_trips = [trips for trips in valid_trips_solutions if len(trips) == min_solution]

    return best_trips
    

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    filename = "ps1_cow_data.txt"
    cows = load_cows(filename=filename)
    t0 = time()
    greedy_algorithm_best_solution = greedy_cow_transport(cows=cows)
    t1 = time()
    print("The greedy cow transport algorithm best solution is: \n", greedy_algorithm_best_solution)
    print("The greedy cow transport algorithm took %f seconds.\n" %(t1 - t0))
    t2 = time()
    brute_force_best_solutions = brute_force_cow_transport(cows=cows)
    print("The brute force algorithm best solutions are: \n", brute_force_best_solutions)
    t3= time()
    print("The brute force algorithm took %f seconds" %(t3 - t2))

compare_cow_transport_algorithms()