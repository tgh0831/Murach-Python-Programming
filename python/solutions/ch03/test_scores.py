#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()

more_tests = "y"

while more_tests.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

    counter = 0
    score_total = 0
    test_score = 0

    while True:
        test_score = input("Enter test score: ")
        if test_score.lower() == "end":
            break
        else:
            test_score = int(test_score)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print("Total Score:", score_total,
          "\nAverage Score:", average_score)

    print()
    more_tests = input("Enter another set of test scores (y/n)? ") 
    print()
    
print("Bye")


