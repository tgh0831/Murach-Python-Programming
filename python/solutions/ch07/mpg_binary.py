#!/usr/bin/env python3

import pickle

# a file in the current directory
FILENAME = "trips.bin"

def write_trips(trips):
    with open(FILENAME, "wb") as file:
        pickle.dump(trips, file)
        
def read_trips():
    trips = []
    with open(FILENAME, "rb") as file:
        trips = pickle.load(file)
    return trips

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven:\t"))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:\t"))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for i in range(0, len(trips)):
        trip = trips[i]    
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips()
    list_trips(trips)
    
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
            
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trips.append(trip)
        write_trips(trips)

        list_trips(trips)
        
        more = input("More entries? (y or n): ")
    
    print("Bye")

if __name__ == "__main__":
    main()

