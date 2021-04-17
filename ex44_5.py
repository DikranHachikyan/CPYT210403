
def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]    

# 1. дефиниция
def generate_squares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == '__main__':
    values = get_squares(10)
    print(f'values = {values}')

    # 2. присвояване на променлива
    n_pow = generate_squares(10)

    print(type(generate_squares))
    print(type(n_pow))
    
    print(f'1 => {next(n_pow)}')
    print(f'2 => {next(n_pow)}')
    print(f'3 => {next(n_pow)}')
    print(f'4 => {next(n_pow)}')
    print(f'5 => {next(n_pow)}')
    print(f'6 => {next(n_pow)}')

    arr = list(n_pow)
    print(f'arr:{arr}')

    sqr_5 = generate_squares(5)
    for i in sqr_5:
        print(f'i = {i}')

    sqr_3 = generate_squares(3)
    print(f'1 => {next(sqr_3)}')    
    print(f'2 => {next(sqr_3)}')    
    print(f'3 => {next(sqr_3)}')    
    print(f'4 => {next(sqr_3)}')    
    print(f'5 => {next(sqr_3)}')    
    print('---')