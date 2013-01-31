def fizzbuzz(n):
    if n % 15 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return str(n)

def print_fizzbuzz(start, end):
    numbers = range(start, end + 1)
    return "\n".join(fizzbuzz(n) for n in numbers)

def main():
    print print_fizzbuzz(1, 100)

if __name__ == '__main__':
    main()