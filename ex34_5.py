# port - глобална променлива
port = 3306 


def show(title, a = 100, *args, kwo1, kwo2 = 'A', **kwargs):
    print(f'title={title}')

    print('optional params:')
    
    print(f'a={a}')

    print(f'args:')
    for v in args:
        print(f'arg:{v}', end = ' ')
    print()

    print('kwargs')
    kw_params = {
        'version': kwargs.get('version', '0.0.1'),
        'n_proc': kwargs.get('n_proc', 5)
    }
    print(f'kw_params:{kw_params}')

    print('keyword-only params:')
    print(f'kwo1 = {kwo1} kwo2 = {kwo2}')


if __name__ == '__main__':
    
    app_config = {
        'version': '1.2.3',
        'n_proc': 10,
        'max_mem': 4096,
        'editors': 10,
        'margins': [5, 5, 10, 10]
    }

    # show('Text Editor', **app_config)
    show('Text Editor', kwo1 = 10, n_proc = 11, version = '2.0.0')
    print('---')