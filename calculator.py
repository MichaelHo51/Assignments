def addition(x,y):
	return (x+y)

def subtraction(x,y):
	return (x-y)

def multiplication(x,y):
	return (x*y)

def division(x,y):
	return (x/y)

def square(x):
	return (x ** 2)

def cube(x):
	return (x ** 3)

def square_n_times(x,y):
	return (x ** y)

print "I will use the calculator to add 333 to 777, then divide that result by 10"
a = addition(333,777)
b = division(a,10)

print a
print b

print "I will use the calculator to square 10, and to cube 5"

c = square(10)
d = cube(5)

print c
print d

print "I will use the calculator to square 5 seven times"

e = square_n_times(5,7)
print e