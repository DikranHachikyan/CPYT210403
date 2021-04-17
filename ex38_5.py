# port - глобална променлива
c = 3306 

def show():
    global c
    
    c = 10
    print(f'c = {c}')


if __name__ == '__main__':
    
    print(f'before c = {c}')
    show()
    print(f'after c = {c}')
    
    print('---')