a = input()
b = input()
c = input()
num = 0

if a != 'FizzBuzz' and a != 'Fizz' and a != 'Buzz':
    num = int(a)+3
elif b != 'FizzBuzz' and b != 'Fizz' and b != 'Buzz':
    num = int(b)+2
elif c != 'FizzBuzz' and c != 'Fizz' and c != 'Buzz':
    num = int(c)+1
else:
    print('oor')

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)