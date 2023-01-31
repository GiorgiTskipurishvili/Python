def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
        else:
            print("Not year")
    else:
        print("Not Leap Year")


if __name__ == '__main__':
    x = int(input("Enter Year: "))
    is_leap_year(x)
