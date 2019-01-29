# If x is odd, print Weird
# If x is even and in the inclusive range of  to , print Not Weird
# If x is even and in the inclusive range of  to , print Weird
# If x is even and greater than , print Not Weird

n = int(raw_input())

if (6 <= n <= 20) or (n % 2 != 0):
    print "Weird"
elif (2 <= n <= 5) or n > 20:
    print "Not Weird"
