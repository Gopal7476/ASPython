# Permutations In Which N People Can Occupy R Seats In A Classroom.

def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

no_of_people = int(input())
no_of_seats = int(input())
print(factorial(no_of_people) // factorial(no_of_people - no_of_seats))