def main():
    print("this program converts US dolars to Georgian Lari")

    dollars = eval(input("Enter amount in dolars?: "))
    lari = convert_to_pounds(dollars)

    print("This is", lari, "Lari")

convert_to_pounds = lambda dollars: dollars * 2.63

main()
