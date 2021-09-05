#Author Raman Mehta
## Read input as specified in the question.
## Print output as specified in the question.
# A recursive Python program
# to check whether a given
# number is palindrome or not

# A recursive function that
# check a str[s..e] is
# palindrome or not.
def isPalRec(st, s, e) :
	
	# If there is only one character
	if (s == e):
		return True

	# If first and last
	# characters do not match
	if (st[s] != st[e]) :
		return False

	# If there are more than
	# two characters, check if
	# middle substring is also
	# palindrome or not.
	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1);

	return True

def isPalindrome(st) :
	n = len(st)
	
	# An empty string is
	# considered as palindrome
	if (n == 0) :
		return True
	
	return isPalRec(st, 0, n - 1);



str=input()
n=len(str)
if isPalindrome(str):
    print("true")
else :
     print("false")
    
