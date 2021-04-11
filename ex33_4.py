# port - глобална променлива
port = 3306 


def show(title, a = 100, *args, **kwargs):
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


if __name__ == '__main__':
    # 1.
    # show('Text Editor')

    # 2.
    # show('Text Editor', 2)

    # 3.
    # show('Text Editor', 2, 11, 12, 34, 56, 6)

    # 4
    app_config = {
        'version': '1.2.3',
        'n_proc': 10,
        'max_mem': 4096,
        'editors': 10,
        'margins': [5, 5, 10, 10]
    }

    # show('Text Editor', **app_config)
    show('Text Editor', n_proc = 11, version = '2.0.0')
    print('---')