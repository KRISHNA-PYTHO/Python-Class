text="Elsa is a good girl"
text1='captain'
text2='         avengers       '

#basic string function
print(text+text1)
print(text1*5)
print("length of string:",len(text))


print()

#string method
print('----string method----')
text="Elsa is a good girl"
print("uppercase:",text.upper())
print("lowercase:",text.lower())
print("casefold:",text.casefold())
print("capitalized:",text.capitalize())
print("title case:",text.title())

print()

#strip method

print('-----strip method----')
text='       avengers    '
print("stripped:",text.strip())
print("left stripped:",text.lstrip())
print("right stripped:",text.rstrip())

#remove the leading characters "abc"from the string

string="abchello, world!"
stripped_string =string.lstrip("abc")
print(stripped_string)

#output: hello, world!


string="abchello, world!"
stripped_string =string.rstrip("ld!")
print(stripped_string)

#output: hello, wor

print()

print('-----starting and ending and replace string-------')

text="Elsa is a good girl"
print("start with 'Elsa': ",text.startswith("Elsa"))
print("End with 'girl': ",text.endswith("girl"))
print("replaced 'Elsa' with 'anna':",text.replace("Elsa","anna"))

print()

#string slicing
print('----silcing of string-----')
print("First 5 characters:",text[:3])
print("last 6 characters:",text[-3:-1])

print()