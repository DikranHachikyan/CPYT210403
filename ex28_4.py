# port - глобална променлива
port = 3306 

# 1. дефиниция на функцията
def sum_numbers(a, b):
    # c - локална за функцията променлива
    c = a + b
    return c


if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5, 6)
    print(f's1 = {s1} ')

    x, y = 10,20
    s1 = sum_numbers(x, y)
    print(f'{x} + {y} = {s1}')
    
    print('---')