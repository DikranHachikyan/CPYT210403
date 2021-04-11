
if __name__ == '__main__':
    app_config = {
        'title': 'Text Editor',
        'version': '1.2.3',
        'n_proc': 10,
        'max_mem': 4096,
        'editors': 10,
        'margins': [5, 5, 10, 10]
    }

    for item in app_config.items():
        key, value = item
        print(f'{key} => {value}')
    else:
        print('-- else --')
        
    print('---')