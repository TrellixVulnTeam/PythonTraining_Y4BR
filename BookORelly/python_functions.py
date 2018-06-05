#lambda is used to create what is known as anonymous functions. These are essentially functions with no pre-defined
# name. They are good for constructing adaptable functions, and thus good for event handling.
# can replace lambda by function
# Python's lambda keyword: unnecessary, occasionally useful.

myfunc = lambda i: i*2
print(myfunc(2))

myfunc = lambda x,y: x*y
print(myfunc(3,6))

def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))

mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*mult3)

def transform(n):
    return lambda x: x + n
f = transform(3)
print("Hold param:",f(4))
