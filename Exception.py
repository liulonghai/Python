__author__ = 'Longhai Liu'


re = iter(range(5))

try:
    for i in range(100):
        print(re.next())

except StopIteration:
    print "Here is the end",i

print 'HaHaHaHa'


try:
    print(a*2)
except TypeError:
    print("TypeError")
except:
    print("Not Type Error & Error noted")


def test_func():
    try:
        m=1/0
    except NameError:
        print("Catch NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print( "Catch error in the main program")

print("LaLaLa")
try:
    raise StopIteration
except StopIteration:
    print "raise StopIteration"
print("LaLaLa")

print("LaLaLa")
try:
    raise StopIteration()
except StopIteration:
    print "raise StopIteration"
print("LaLaLa")