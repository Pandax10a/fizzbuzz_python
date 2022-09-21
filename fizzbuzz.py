def fizzbuzz(the_num):
    for num in array_nums:
        if(((num % 5) == 0) and ((num % 3) == 0)):
            print('this ', num, 'is FizzBuzz')
        elif((num % 5) == 0):
            print('this ', num, 'is Buzz')
        elif((num % 3) == 0):
            print('this ', num, 'is Fizz')

array_nums = [11, 15, 18, 24, 25, 33, 47, 68, 70, 75, 77, 81, 83, 85, 87, 89, 91, 93, 95, 97, 100, 103, 105, 106]

fizzbuzz(array_nums)