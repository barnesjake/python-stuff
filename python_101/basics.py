### numbers
2 + 2

(50 - 5*6) / 4

17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
7 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder

5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7


width = 20
height = 5 * 9
width * height

### strings
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.' # '"Yes," they said.'
"\"Yes,\" they said." # '"Yes," they said.'
'"Isn\'t," they said.' # '"Isn\'t," they said.'

'"Isn\'t," they said.' # '"Isn\'t," they said.'
print('"Isn\'t," they said.') # prints "Isn't," they said.
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output, i.e. 'First line.\nSecond line.'
print(s)  # with print(), \n produces a new line e.g:
#First line.
#Second line.

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote is a raw string

# string literal
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
# 'unununium'

'Py' 'thon' # 'Python'

# this only works with literals, for variables or variable and literal, use +
text = ('Put several strings within parentheses '
         'to have them joined together.')
print(text) # 'Put several strings within parentheses to have them joined together.'


word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

word[-1]  # last character
word[-2]  # second-last character

word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

#s[:i] + s[i:] is always equal to s
word[:2] + word[2:] # 'Python'
word[:4] + word[4:] # 'Python'

# an omitted first index defaults to zero
word[:2]   # character from the beginning to position 2 (excluded)

s = 'supercalifragilisticexpialidocious'
len(s) # 34

### lists
