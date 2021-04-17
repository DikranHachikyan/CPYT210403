# port - глобална променлива
port = 3306 


def show(a, *args, b = 100):
    print(f'a = {a} b = {b}, args = {args}')
    


if __name__ == '__main__':
    
    show(2)

    show(2, b = 5)

    show(2, 9, 8, 7, 6,  b = 5)

    show(2, 9, 8, 7, 6)

    print('---')