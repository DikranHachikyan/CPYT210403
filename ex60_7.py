class ParamNotFoundError(Exception):
    pass

def find_key(key, **kwargs):
    if key not in kwargs:
        raise ParamNotFoundError(f'paramter {key} not found')

    print(f'{key} => {kwargs[key]}')
 

if __name__ == '__main__':

    con = {
        'host':'localhost',
        'port': 3306,
        'service': 'mysqld'
    }
    try:
        find_key('host', **con)
        find_key('ip', **con)
    except ParamNotFoundError as e:
        print(f'missing config parameter ({e})')
    
    print('---')