__author__ = 'Longhai Liu'


re = iter(range(5))

try:
    for i in range(100):
        print(re.next())

except StopIteration:
    print "Here is the end",i


print 'HaHaHaHa'