

if __name__ == '__main__':
    
    actions = {
        '+': lambda a, b: a + b
    }

    try:
        val1 = float(input('first number:'))
        op = input('action (+):')
        val2 = float(input('second number:'))

        print(f'{val1} {op} {val2} = {actions[op](val1,val2)}')
    
    except ValueError as e:
        print(f'invalid number ({e})')
    
    except KeyError as e:
        print(f'invalid action ({e})')
    
    except Exception as e:
        print(f'unknown error ({e})')
    


    print('---')