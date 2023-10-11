fav_band = 'Green Day'
print(fav_band[6])

#first six letters
print(fav_band[:6])

''' 
str doesn't support item assignent
!x: fav_band[6] = 'M'
'''

# e.gs. of methods

text = 'uppercase me'
text_cap = text.upper() #or .lower()
print(text_cap)

# e.g., of True or False check, e.g., if user enters digits only with *.isnumeric*
user_number = input('please provide a number: ')
if user_number.isnumeric():
    print("That's a number!")
else:
    print(user_number, "is not a number!")