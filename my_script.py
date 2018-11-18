import sys
string = sys.argv[2]
substring = sys.argv[1]
occurence = string.count(substring)
print('String {} occured {} times in string {}'.format(substring, occurence, string))

