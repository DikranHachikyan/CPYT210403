# port - глобална променлива
port = 3306 


def show(a, *, b = 100):
    print(f'a = {a} b = {b}')
    


if __name__ == '__main__':
    
    show(2)

    show(2, b = 5)

    print('---')