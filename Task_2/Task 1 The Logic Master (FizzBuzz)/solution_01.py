def fizzbuzz_checker(limit):

    for number in range(1, limit+1):
        if number %3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 ==0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz_checker(30)

