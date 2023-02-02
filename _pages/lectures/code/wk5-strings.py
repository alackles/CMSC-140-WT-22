#instring = input()

# Reversing a string
def reverse(s):
    r = ""
    for i in range(len(s)):
        # what do I do here?
        r += s[len(s) - i - 1]
    return r # what do I return? 

#print(reverse(instring))

# escapes

examplestr = "This doesn't work"
examplestr2 = 'This "string" is okay'

esc_double = "This is \"okay\" now"
twoslash = "\\"

rawstring = r'This prints \' \\\\ exactly what you say \"'
print(esc_double)
print(twoslash)
print(rawstring)

trip_quotes = ''' This is a string \\
across multiple lines
'''
trip_quotes_two = """ hello
"""

"hello"

newline = "This a string\nwith a newline"
print(trip_quotes)
print(trip_quotes_two)
print(newline)

name = "Acacia Lee Ackles"
print(name[0])
print(name[0:6])

# list assignment
my_list = [2, 4, 5]
my_list[0] = 8
print(my_list)

name = "B" + name[1:]
print(name)

print(4 in my_list)

if 5 not in my_list:
    print("Five not found")

if "Lee" in name:
    print("Middle name found")

space_string = "  \t     Hello   \n   "
print(space_string)
print(space_string.strip()) # not in-place! this is a new string!
print(space_string)
print("Lstrip:")
print(space_string.lstrip()) # from the left
print("Rstrip:")
print(space_string.rstrip()) # from the right

cool_string = "~~~~~~hello~~~~~~~"
print(cool_string)
print(cool_string.strip("~"))
print(cool_string.strip("el"))

example_string = "JoyJoyJoySad_oJ"
print(example_string.strip("Joy"))
"\n" # newline
"\r" # return

sentence = "Let's get rid of whitespace"
new_sentence = "".join(sentence.split(" "))
print(new_sentence)

check_email = "acacia.ackles@lawrence.edu".endswith(".edu")
check_name = "acacia.ackles@lawrence.edu".startswith("katie")
print(check_email)
print(check_name)

if check_email:
    print("This is an educational address")