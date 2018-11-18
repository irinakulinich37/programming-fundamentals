import sys
string = sys.argv[1]
vowels = 'aueoi'
for x in string:
    if x in vowels:
        occurence = string.count(x)

print('String {0} contains {1} vowels'.format(string, occurence))