'''
# *in* operator checks every element in string 
for char in 'happy message':
    print(char)

# *in* operator checks every element in list
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')

    #also works: 8. *if name not in invited_guests:
'''