import copy

class Time(object):
    """ 
    """

def print_time(t):
    print "%2.d:%.2d:%.2d" % (t.hour, t.minute, t.second)

# Exercise 16.2.
def is_after(t1, t2):
    s1 = t1.hour*3600 + t1.minute*60 + t1.second
    s2 = t2.hour*3600 + t2.minute*60 + t2.second
    return s1 > s2

# Exercise 16.3.
def increment(t, second):
    t.second += second

    t.minute += t.second/60
    t.second = t.second%60

    t.hour += t.minute/60
    t.minute = t.minute%60

# Exercise 16.4.
def increment_pure(t, second):
    tout = copy.deepcopy(t)
    increment(tout, second)
    return tout

def time_to_int(t):
    return t.hour*3600 + t.minute*60 + t.second

def int_to_time(sec):
    t = Time()
    t.minute, t.second = divmod(sec, 60)
    t.hour, t.minute = divmod(t.minute, 60)
    return t

# Exercise 16.5.
def increment_pure2(t, second):
    return int_to_time(time_to_int(t) + second)

def valid_time(t):
    if t.hour < 0 or time.minute < 0 or time.second < 0 or t.minute >= 60 or t.second >= 60:
        return false
    else:
        return true 

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError, 'invalue time in add_time()'

    s = time_to_int(t1) + time_to_int(t2)
    return int_to_time(s)


def main():
    t1 = Time()
    t1.hour = 0
    t1.minute = 59
    t1.second = 30

    t2 = copy.deepcopy(t1)
    t2.second = 31


    print_time(t1)
    print_time(t2)

    print is_after(t2, t1)
    print is_after(t1, t2)


    print "\nincrement t1 and t2"
    increment(t1, 600)
    increment(t2, 3600)
    print "t1 : ",
    print_time(t1)
    print "t2 : ",
    print_time(t2)


    print "\npure increment:"
    t3 = increment_pure(t2, 3600)
    print "t2 : ",
    print_time(t2)
    print "t3 : ",
    print_time(t3)

    t4 = increment_pure2(t2, 29)
    print "t2 : ",
    print_time(t2)
    print "t4 : ",
    print_time(t4)


main()

