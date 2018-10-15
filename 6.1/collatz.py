def collatz(number):
    try:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            else:
                number = (3 * number + 1)
                print(number)
    except (NameError, TypeError) as e:
        print("Please enter an integer! {}".format(e))


number = int(input("Enter number: "))

collatz(number)
