def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # pass
        raise 
        # print(f'invalid key {key} ({e})') 

if __name__ == '__main__':

    con = {
        'host':'localhost',
        'port': 3306,
        'service': 'mysqld'
    }
    try:
        find_key('host', **con)
        find_key('ip', **con)
    except KeyError:
        pass
    
    print('---')