def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number

def main():
    for i in range(0,101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
