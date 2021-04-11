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
    if 'version' in kwargs:
        print(f'version:{kwargs["version"]}')
    if 'n_proc' in kwargs:
        print(f'n_proc:{kwargs["n_proc"]}')


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

    show('Text Editor', **app_config)
    
    print('---')