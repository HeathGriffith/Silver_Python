# If a function that raises an exception doensn't have a try-except block,
#   that exception is propogated to the function that called it. If that function doesn't have a try-except block,
#       the exception will continue to be propogated down the function-call chain

def get_day(user_info):
    day = int(input("What's the day of your bday? "))
    user_info.append(day)

def get_month(user_info):
    month = int(input("What's the month (1 - 12) of your bday? "))
    user_info.append(month)

def get_year(user_info):
    year = int(input("What's the year of your bday? "))
    user_info.append(year)

def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print("So your bday is", user_info)
    except ValueError:
        print("You entered incorrect data. Bye.")

print("Hi, I'll collect info about your bday.")
user_info = []
get_user_bday(user_info)
