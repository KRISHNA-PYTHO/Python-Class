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

