
if __name__ == '__main__':
    lst = [ x ** 2 for x in range(10)]
    lst2 = [ f'{x} {y}' for x in range(5) for y in range(5)]
    
    print(f'values:{lst}')
    print(f'values2:{lst2}')
    
    txt = 'Lorem ipsum dolor sit amet'

    letters = [ f'[{t}]' for t in txt]
    print(f'letters:{letters}')
    
    print('---')