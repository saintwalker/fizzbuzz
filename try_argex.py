import sys

while True:
	if len(sys.argv) < 2:
		try:		
			upper_bound = int(raw_input("Please enter a number that will be the upper bound for this fizzbuzz game: "))
		except ValueError:
			print "Sorry, we need an int for this to run."
		except NameError:
			print "Sorry, that's not a valid int for the upper bound."
	else:
		try:
			upper_bound = int(sys.argv[1])
			print "You have entered a maximum number of : ", str(sys.argv[1])
		except ValueError:
			print "You have entered a non-integer value for the upper bound"
		except NameError:
			print "Sorry, that's not a valid int for the upper bound."
	break

print "Fizz counting up to " + str(upper_bound)

current_number = 0

while current_number < upper_bound:

        print current_number

        if current_number%3 == 0 and current_number%5 != 0:

                print "fizz"

        if current_number%5 == 0 and current_number%3 != 0:

                print "buzz"

        if current_number%5 == 0 and current_number%3 == 0:

                print "fizz buzz"

        current_number += 1
