def foo(c):
    c = 10
    print(f'c = {c}')

def show(values):
    values.sort()
    print(f'show:{values}')

if __name__ == '__main__':
    numbers = [5, 4, 3, 2, 1, 9, 8, 7]
    x = 100
    # foo(x)
    # print(f'x = {x}')

    show(numbers)
    print(f'numbers:{numbers}')
    print('---')