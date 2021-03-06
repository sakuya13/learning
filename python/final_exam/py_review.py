
'''
general
'''
# returns a list of iterables (keys in this case):
sorted({'dogs': ['Anne'], 'ducks': ['Mathew']})

# sort or max with the value
d={'dogs':['P'],'ducks':['M']}
print(sorted(d))  # by default: sort with key
print(sorted(d, key=lambda k: d[k]))  # 
# if you want to return the key and the value
print(sorted(d.items(), key=lambda k: k[1]))  # sort with value

# TODO:enumerate
for index, number in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    if index == 5:
        continue
    if index == 8:  # it won't print value A[8], break before print
        break
    print(number, end=' ')
print('end')  # the 'end' will follow the numbers, because of end=' '

for index, number in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(index, number)

# rounding error
a = 12345678901234567890
b = 0.1
c = a + b - a
print(c)

# float modular
print(3.1 // 1.5)
print(3.1 % 1.5)
print((3.1 // 1.5) * 1.5 + 3.1 % 1.5)

# TODO:boolean: all false
bool(0)
bool(())
bool([])
bool({})
bool(set())

# comparing strings
print('he' < 'hi')
print('Hell' >= 'Hello')
print('h' > 'H')
print('Z' < 'a')
print(ord('a'))
print(ord('A'))
print('a'>'A')

# Should be false
print('le' in 'Hello')
# TODO: The empty string is in everything
print('' in 'Hello')

# in > not > and > or
print(not 1 > 2 and 1 > 0 or "din" in "coding")
print("Monday" and not "holiday" and not "birthday")
n = 4
print((0 < n) and (n < 6))
print(0 < n < 6)
print('A' < 'Z' < 'a')

# while loop controlled by slicing
word = "rendezvous"
while word:
    if word[0] == 'z':
        word = word[1:]
        break
    word = word[1:]
print(word)

# docstring
def maxl(lst):
    """
    maxl takes a nonempty list lst, and returns the maximum element 
    of that list.
    """
    return lst[0] if len(lst)==1 else \
    (lst[0] if lst[0]>maxl(lst[1:]) else maxl(lst[1:]))
help(maxl)

# TODO:
s = 'wumbly'
s[:1:-1]
s[1:3:-1]  # if -1, the left one should be bigger than the middle one
s[:2:-1]
s[3:1:-1]
s[-1:-5:-1]

# list multiplication
my_list = [1, 2, 3] * 5
print(my_list)

# len tuple
empty = ()
print(len(empty))
single = (3,)
print(len(single))

# dict getTODO: d[k] if k in d, else return by default None
my_dict = {"Age":34,"Anna":"Joe","Jobs":"Steve"}
print(my_dict.get("fat"))
print(my_dict)
print(my_dict.pop('fat'))  # second arguement not given, keyError
print(my_dict)

# del and clear
my_dict = {"Age":34,"Anna":"Joe","Jobs":"Steve"}
del my_dict["Age"]
print(my_dict)
my_dict.clear()
print(my_dict)

# TODO: 
pi = 3.1415
print('{:6.2f}'.format(pi))
pi = '3.1415'
print('{:10s}'.format(pi))

'''
week02
1. variable naming: must not start with a number, but can contain numbers in the
rest part of the name.

2. With two exceptions, operations of equal precedence are left associative,
so they are evaluated from left to right. Exponentiation (**) and assignment (=)
are right associative.

3. the escape sequeces: \b, \n, \t, \\, \', \"
'''
print('a\b')  # should print a
print('a\bb')  # should print b only

a = ''  # a is string
chr(ord('a')+3) #  shifting in ASCII
-3**2
-(3)**2  #  lecture note is wrong
(-3)**2

# TODO: only exponentiation and assignmment are right associative
2 ** 3 ** 2  # 512
(2 ** 3) ** 2 # 64

# float or int?
x//12.0
3//2*5.0
3/2*5
4//3**2  # exponentiation is higher than //
# differences? how to call the functions?
import math
from math import pi, sqrt
from math import *

# result?
int(3.77)
int('3.77')
round(3.77)

# multi-line paragraphs
print('''abcabc
abcabc''')
# actually means:
print('abcabc\nbcabc')

# multiply str
print(' '*10 + 'abc')

'''
week03
1. precedence of  logical operators: 'not' is higher than 'and', 'or' (p.41)
'''
a = False  #  b = true or false
a and b  # only need to evaluate a
a = True
a or b  # only need to evaluate a

'''
week04
1. string is an immutable data structure.
2. string methods s.split()
'''
# what's the result?
s = 'abcdef'
print(s[2::-1])
print(s[2:0:-1])
print(s[-4:-6:-1])
print(s[0:2:-1])  # TODO:is it gonna return error? empty string
print(s[1: -1])
# string methods
s.center(width)  # with is the length of the intended string
s = 'hi'
print(s.center(11))

s.count(sub[, start[, end]])
s = 'aabbbccccc'
print(s.count('c', 0, 6))
print(s.endswith('c'))
print(s.startswith('aab'))
print(s.isalpha())

s.lower()
s.upper()
s.endswith(sub)
s.startswith(sub)
s.isalpha()
s.isdigit()

s.join(sequence)  #', '.join(list), s is the separator string
print(', '.join(['abcd', 'efgh']))  # here the separator is , and whitespace
print(' '.join(['abcd', 'efgh']))  # here the separator is whitespace

s.find(sub[, start[, end]])  # return the lowest index, can't find then return -1
quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.find('hings', 10))
# Substring is searched in 'hings with great lov'
print(quote.find('lov', 10, -1))

s.replace(old, new[, count])  # only the first count occurrences are replaced
s = 'Hi There'
print(s.replace('i', 'o'))
song = 'let it be, let it be, let it be'
# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))
print(song.replace('let', 'so', 2))

song = 'let it be, "let" it be, let it be.'
print(song.split())
new_song = song.split()
word_list = [item.rstrip(',').rstrip('.').strip('\"').strip('\'')\
            for item in new_song]
print(word_list)

s.split([sep])  # sep is the dilimiter, by default use whitespace as dilimiter,
# returns a list.
s.strip([aString])  # by default remove the leading and trailing whitespace
s.rstrip()  # remove trailing
s.lstrip()  # remove leading

'''
week05
'''
# for loop print without newline
for character in 'Hi there!':
    print(character, end=' ')

# step value in range
list(range(1, 6, 2))

# enumerate
text = 'simple'
for index, character in enumerate(text):
    print(index, character, end=' ')
print('end')

# mid-term test: loop control statements
for index, number in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    if index == 5:
        continue
    if index == 8:
        break
    print(number, end=' ')
print('end')

# nested loop: find prime number
for num in range(1,20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, j, i))
            break
    else:
        print(num, 'is a prime number.')
# alternative way
for num in range(1,20):
    loop_done = True
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, j, i))
            loop_done = False
            break
    if loop_done:
        print(num, 'is a prime number.')

'''
formating old ver.
'''
# '%<format string>' % (<datum-1>, ..., <datum-n>)
print('%6s' % 'four')  # right justified
print('%-6s' % 'four')  # left justified

for exponent in range(7, 11):
    print('%-3d%12d' % (exponent, 10 ** exponent))

# formatting float: '%<field width(precision included)>.<precision>f' % (<datums>)
print('%6.3f' % 3.14)
print(str(100.00))  # by default, precision to 0.1

'''
week06 formatting continue
'''
'''old ver'''
# formatting won't round
amount = 24.325
print('%.2f' % amount)
# guess it
print('%5s' % 'tropical')
print('%.5s' % 'tropical')
print('%5s' % 'trop')
print('%-5s' % 'trop')

x=1
y=2
z=3
print('%6d\n%6d\n%6d' % (x, y, z))
print('%-6d\n%-6d\n%-6d' % (x, y, z))

s = 'mysterious'
print('%.*s' % (7, s))  # 7 characters in the string
print('%.*s' % (2, s))

# TODO: scientific notation
print('%10.3e' % 2000.345)
print('%10.2E' % 2000.345)

# negative numbers(or showing the sign)
print('%+d' % 60)  # positive num sign inside the format string, negative is not
print('%d' % -60)

'''
new formatting
'''
print('{:_<10}'.format('test'))
print('{:_^10}'.format('test'))
print('{:_>10}'.format('test'))
print('{:*<10}'.format('test'))  # TODO: left justified, so the * should append to the right
print('{:f}'.format(3.141592653589793))  # by default, precision to 0.000000
print('{:10s}'.format('this is')) #default left justified

print('{:e}'.format(0.00002))

print('{:+d}'.format(60))
print('{:d}'.format(-60))

data = [4, 8, 15, 16, 23, 42, 34, 65, 12]
print('{d[4]} {d[5]}'.format(d=data))

print('{0} is {0:b}'.format(128))  # convert to binary form
print('{0} is {0:o}'.format(128))  # convert to 8 bit
print('{0} is {0:d}'.format(128))  # convert to 10 bit
print('{0} is {0:x}'.format(128))  # convert to 16 bit

from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2016, 2, 10, 4, 30)))

'''week7&8'''
list1 = [1,2,3]
list2 = [4,5,6]
list1 + list2  # list2 append to the end of list1

# list comparision: returns true if comparision of each elements of the
# corresponding position is true
list2 > list1

# mutable: replacing an element in a list
l1[2] = 7  #  l1 will be [1,2,7]

sentence = 'This example has five words.'
words = sentence.split()
index = 0
while index < len(words):
    words[index] = words[index].upper()
    index += 1
print(words)

# TODO: substitute a slice of the list
num = [1, 2, 3, 4, 5]
num[0:3] = [11, 12, 13]
print(num)

'''list.methods()'''
'''lst.index(item)  #  similar to string method find'''
# search an item using index
lst = [1,2,3,4,5]
target = 3
if target in lst:
    print(lst.index(target))
else:
    print(-1)

'''lst.append(item)  #  it does not return a list'''
# use user input to control a loop
name_lst = []
again = 'y'
while again =='y':
    name = input('enter name: ')
    name_lst.append(name)
    print('do you want to add more name?')
    again = input('y = yes, anything else = no: ')
print('name list: ', name_lst)

'''lst.sort() rearrange items in ascending order'''
example = [10,5,23,6]
example.sort()  # can be used to sort the list and find the median
print(example)
# using sorted() method, which will return the sorted list, but won't change
# the original list
example = [10,5,23,6]
print(sorted(example))
print(example)

'''lst.insert(<index>,<item>) it won't delete or replace the items in the lst'''
lst = [2,54,4,3,5]
lst.insert(2, 'fat')
print(lst)

'''list.reverse()'''
example = [10,5,23,6]
example.sort()
example.reverse()
print(example)
# example to use the reverse function
listofvalues = [10,5,23,6]
for i in reversed(listofvalues):
       #print (i)
       print('{:#^10d}'.format(i))
print("####")

'''lst.extend()'''
example = [10,5,23,6]
extra = [1, 2, 3]
example.extend(extra)
print(example)

'''TODO: lst.remove(item)  note that you need to know the item'''
example = [10,5,23,6]
example.remove(5)  # if item not in the list, will trigger a ValueError
print(example)

'''TODO: del <list[index]>  don't have to know the item'''
example = [10,5,23,6]
del example[2]
print(example)

'''max(<list>) and min(<list>)'''
example = [10,5,23,6]
print(max(example))

'''list comprehension'''
s = [x ** 2 for x in range(10)]
print(s)
v = [2 ** i for i in range(13)]
print(v)
lst = list(range(10))
m = [x for x in lst if x % 2 == 0]
print(m)


# one way to find prime numbers
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)
# alternative way without using list comprehension
noprimes = []
for i in range(2, 8):
    for j in range(i*2, 50, i):
        noprimes.append(j)
print(noprimes)
primes = []
for x in range(2, 50):
    if x not in noprimes:
        primes.append(x)
print(primes)

# another example
words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [(w.upper(), w.lower(), len(w)) for w in words]
print(stuff)

# this type of for loop can be replaced by list comprehension
tally = {'2000': 21, '2001':21, '2002':20, '2003':19}
max_list = []
tally_max = max(tally, key=lambda k: tally[k])
for item in tally:
    if tally[item] == tally[tally_max]:
        max_list.append(item)
print(', '.join(max_list))

# better use list comprehension:
tally_max = max(tally, key=lambda k: tally[k])
m_lst = [item for item in tally if tally[item] == tally[tally_max]]
print(', '.join(m_lst))

'''TODO:三目操作符'''
print('fat' if 'fat' == 'fat' else 'cat')

'''TODO: aliasing and side effects'''
first = [1,2,3]
second = first
second.append(5)
print(first)
print(second)
print('second is first?', second is first)
second = [4,5,6]  # assign second to a new object, now have nothing to do with first
print(second)
print('second is first?', second is first)
#  prevent from aliasing, side effects. two ways:
first = [1,2,3]
third = first[:]
third.append(4)
print(first)
print(third)
print('third is first?', third is first)
#  alternative way:
first = [1,2,3]
third = []
for element in first:
    third.append(element)
print(first)
third[1] = 5
print(third)
print('third is first?', third is first)

# object identity and structural equivalence
lst1 = [1,2,3]
lst2 = [1,2,3]
print(lst1 == lst2)  #  true
print(lst1 is lst2)  #  false
#  however, if we do this:
lst1 = lst2
lst1 == lst2  #  true
lst1 is lst2  #  true

'''TODO: tuples immutable, operations: concatenation, iteration, in, slicing,
indexing are allowed, cannot update, cannot remove individual tuple
elements(but able to delete the entire tuple)'''

example = ['fat', 'cat']
print(tuple(example))  # covert the list into a tuple
print(example)

# creating tuples: must contain a comma
tup = (50)
tup2 = (50,)

# accessing is the same as list
tup1 = (1,2,3)
print(tup[1])

# deleting the entire tuple is allowed
tup1 = (1,2,3)
del tup1
print(tup1)  # will trigger a NameError

# min, max, len are allowed
max(tup1)
min(tup1)
len(tup1)

'''dictionary: dictionary TODO:keys(must be immutable data type since python3)
can be data of any immutable types(string, tuple). any data type which has
__hash__ (hashable) and __eq__ (comparable) methods can be key
(set has same requirement). associated values can be of any type'''
'''In short this means you can use: int, float, str, tuple, bool as keys,
but you cannot use: list, set. '''
'''all python built-in immutable data type are hashable, mutable types are not.
frozen set are also immutable and hashable, can be used as a dictionary key.
all of the above can be used as the default arguement of a function'''

# TODO: last d[2] is kept
d = {1:0, 2:0, -1:4, "hello":0, 9:9, 2:2, 2:3}
print(list(d.items()))

'''<dictionary>[key] = <value>  add or replace value in a dictionary'''
info = {}
info['name'] = 'Sandy'
info['occupation'] = 'hacker'
print(info)
#  replace value
info['name'] = 'cat'
print(info)

# dictionary methods
employee_record = {'name': 'kevin',
                   'Age': 43,
                   'ID':23145,
                   'payrate':24.99
                  }
employee_record2 = {'name': [1, 2, 3, 4],
                   'Age': [43, 23, 34, 45],
                   'ID': 23145,
                   'payrate': 24.99
                  }
# one way of getting all items:
for key, value in employee_record.items():
    print(key, value)
# another way:
for key in employee_record:
    print(key, employee_record[key])
# getting all keys
print(list(employee_record.keys()))
for key in employee_record.keys():
    print(key)
# get all value
print(list(employee_record.values()))
for value in employee_record.values():
    print(value)
# employee_record.values() 
# returns 'dict_values([[1, 2, 3, 4], [43, 23, 34, 45], 23145, 24.99])'
# deleting an item
del employee_record2['Age']
# TODO: pop(), second arguement is the default value, if no such key, then return this
# value. if not this value is not assigned, trigger KeyError.
print(employee_record2.pop('Age', 'not found'))

# test if a key is in a dictionary
a = 'name'
if a in employee_record:
    print('a is in the dictionary')
else:
    print('not found')

'''TODO: default dictionary'''
from collections import defaultdict
def hapax(text):
    t_list = text.split()
    d = defaultdict(int)  # the parameter here is the type for value
    for word in t_list:
        d[word] += 1
    sorted_d = sorted(d)
    freq_1_word = [key for key in sorted_d if d[key] == 1]
    return freq_1_word

print(hapax('a b c a'))
print(hapax('c ba a a'))

# an example with the list as the value type
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)

# Note also that the type we provide is only the default value for a new key,
# and we are not constrained to use only that type for all {key: value} pairs:
# also can use import as if the method name is very long
from collections import defaultdict as dd
d = dd(int, {'a': 2})
d['b'] = 'hah!'
print(d)

'''set
TODO: SET union the two set: "|", find the intersection:"&".
SET has random order'''
my_set={"a", "b", "c", 1, 0}
print("a" in my_set)
print(True in my_set)
print(False in my_set)

my_sequence = "hello"
my_set = set(my_sequence)
print(my_set)

my_set1 = {2, 3, 4}
my_set2 = {2, 5}
print("my_set1 - my_set2", my_set1 - my_set2)
print("my_set2 - my_set1", my_set2 - my_set1)
print("Union: my_set2 | my_set1", my_set2 | my_set1)
print("Intersection: my_set2 & my_set1", my_set2 & my_set1)

my_set = {"a", 1, ("bob", 45)}
my_set.add(("Joe", 50))
print(my_set)  # set has no order(every time generates different order)
my_set.remove(("bob", 45))
print(my_set)

my_set = {"a", 1, ("bob", 45)}
print(len(my_set))

# Q, P3 TODO: set.update()
def make_catalogue(items, old_cat=None):
    itemset = set(items)
    if isinstance(old_cat, set):
        old_cat.update(itemset)  # update the set with the union of itself and others
        # return old_cat.copy()
        return set(old_cat)  # return a new set but not the original set
    return itemset
    # if old_cat is not None :
    #     return   # Union the two sets
    # else:
    #     return set(items)
def debug():
    print(make_catalogue(['spam', 'spam', 'eggs']))
    print(make_catalogue(['spam','spam','eggs'], old_cat={'eggs','milk'}))
    my_cat = {'spam', 'socks'}
    print(make_catalogue(['toothbrush', 'socks'], my_cat))
    print(my_cat)
debug()

'''week09 functions'''

n = -4.55
def print_digits(n):
    s = str(abs(n))
    print(len(s) - ('.' in s))  # boolean automated converted to 1 or 0
print_digits(n)

True - 1  # whats the result?
False - 1

def digit(n):
    s = str(abs(n))
    return len(s) - ('.' in s)
print(digit(-4.55e05))  #  this is a float
print(digit(-455000.0))  # scientific notation, will keep the float type
print(digit(-4.55e-05))  # scientific notation, will keep the float type
print(digit(-0.0000455))  # scientific notation, will keep the float type
print(digit(-4.55))


'''week10 file I/O'''
file = open('test.txt', 'r')
file.read()  # read whole file
file.readline()  # read only one line a time
line = line.rstrip('\n')  # readline will keep a \n at the end of each line
file = open('test.txt', 'w')
file = open('test.txt', 'a')
file.write('fat and cat')
file.close()

# alternatively: automatically close when the block finishes
with open('test.txt', 'w') as filename:
    filename.write('fat and cat')
    for line in filename:  # use for loop to iterate the file
        lines = line
        print(lines)

# read numbers
# suppose each line in the file contains only one integer
with open('integers.txt', 'r') as txtfile:
    sums = 0
    for line in txtfile:
        line = line.strip()
        number = int(line)
        sums += number
    print('The sum is:',sums)
# suppose each line contain multiple integers
with open('integers.txt', 'r') as txtfile:
    sums = 0
    for line in txtfile:
        integer_list = line.split()
        for integer in integer_list:
            number = int(integer)
            sums += number
    print('The sum is:',sums)

