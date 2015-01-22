to_number = 100
print "Fizz counting up to " + str(to_number)
current_number = 0

while current_number < 100:
	print current_number
	if current_number%3 == 0 and current_number%5 != 0:
		print "fizz"
	if current_number%5 == 0 and current_number%3 != 0:
		print "buzz"
	if current_number%5 == 0 and current_number%3 == 0:
		print "fizz buzz"
	current_number += 1
