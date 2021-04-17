# port - глобална променлива
port = 3306 


def show(a, b = 100, *args):
    print(f'a = {a} b = {b}, args = {args}')
    


if __name__ == '__main__':
    
    show(2)

    show(2, 5)

    show(2, 5, 9, 8, 7, 6)

    show(2, 9, 8, 7, 6)

    print('---')