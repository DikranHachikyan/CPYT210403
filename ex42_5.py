def foo(a = None, b = None):
    if not a: a = []
    if not b: b = {}
    
    print(f'a = {a}')
    print(f'b = {b}')
    print(' - ' * 20)
    n = len(a)
    a.append(n)
    b[n] = n
    

if __name__ == '__main__':

    foo()
    foo([5,2,1], {'x':10})
    foo()
    foo([15,21,11], {'x':100})
    foo()
    print('---')