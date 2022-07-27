# logical conditions python
# equals: a == b
# not equals: a != b
# less than: a < b
# less than or equal to: a <= b
# greater than: a > b
# greater than or equal to: a >= b

a = 200
b = 20
c = 100

#if a > b:
#    print("a greater than b")
#elif a == b:
#    print("a and b are equal")
#else:
#    print("a less than b")

#if a < b and a < c: #and
#    print("Both conditions are True")
#elif a < b  or a < c: #or
#    print("At least one of the conditions is True")

#nested if
if a > b:
    print("a lebih besar dari b")
    if a > c:
        print("a juga lebih besar dari c")
else:
    print("a tidak lebih besar dari b dan c")