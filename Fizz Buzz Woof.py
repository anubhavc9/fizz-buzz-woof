n = int(input("Enter value of n: "))
key = {3: 'Fizz ', 5: 'Buzz ', 7: 'Woof '}
for i in range(1, n+1):
    change = False
    for j in key:
        if i % j == 0:
            count = str(i).count(str(j))
            count += 1
            change = True
            print(key[j]*count, end='')
        elif str(j) in str(i) and i % j != 0:
            change = True
            times = str(i).count(str(j))
            print(key[j]*times, end='')
    if not change:
        print(i, end='')
    print()