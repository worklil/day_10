# from replit import clear

should_continue = True
while should_continue:
    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Leap year.")
                    return True
                else:
                    print("Not leap year.")
                    return False
            else:
                print("Leap year.")
                return True
        else:
            print("Not leap year.")
            return False



def days_in_month(year, month):
    # if month > 12 or month < 1:
    #     return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    print(month_days[month - 1])



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year=2022, month=2)
print(days)