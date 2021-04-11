
if __name__ == '__main__':
    app_config = {
        'title': 'Text Editor',
        'version': '1.2.3',
        'n_proc': 10,
        'max_mem': 4096,
        'editors': 10,
        'margins': [5, 5, 10, 10]
    }

    for key in app_config:
        print(f'{key} => {app_config[key]}')
        
    print('---')