# Python3 program to get the
# total number of guests at the party

# Function to find the totalGuests
def findGuest(guests, N):
	count = 0

	# Checking requirements for each guest
	for i in range(N):

		# If requirements are met
		if guests[i] <= count:

			# The Gi guest decides to stay
			# So increment total guest by 1
			count += 1
			
	# Return the totalnumber of gues
	return count

# Driver code
N = 5
guests = [1, 0, 2, 1, 3]
totalGusets = findGuest(guests, N)
print(totalGusets)

# This code is contributed by Shrikant13
