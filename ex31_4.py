# port - глобална променлива
port = 3306 

# 1. дефиниция на функцията
def sum_numbers(a, b, *args):
    # c - локална за функцията променлива
    print(f'args:{args}')
    c = a + b
    for v in args:
        c += v

    return c


if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5, 6)
    print(f's1 = {s1} ')

    x, y, z, m, n = 10, 20, 3, 6, 8
    s1 = sum_numbers(x, y, z, m, n)
    print(f'{x} + {y} + {z} + {m} + {n} = {s1}')
    
    values = [ i for i in range(5, 10)]
    s1 = sum_numbers(x, y, *values)
    print(f'{x} + {y} + ' + ' + '.join(map(str, values)) + f' = {s1}')
    print('---')