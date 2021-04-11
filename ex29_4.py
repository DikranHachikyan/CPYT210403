# port - глобална променлива
port = 3306 

# 1. дефиниция на функцията
def sum_numbers(a, b, d = 0):
    # c - локална за функцията променлива
    c = a + b + d
    return c


if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5, 6)
    print(f's1 = {s1} ')

    x, y, z = 10, 20, 3
    s1 = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {s1}')
    
    print('---')