
def sort_priority(values, group):
    found = False

    def sort_helper(el):
        if el in group:
            nonlocal found
            found = True
            return (0, el)
        
        return (1,el)

    values.sort(key=sort_helper)
    return found

if __name__ == '__main__':
    numbers = [5, 4, 3, 2, 1, 9, 8, 7]

    grp = {4,8,9} 
   
    is_found = sort_priority(numbers, grp)

    print(f'is_found = {is_found}  numbers:{numbers}')
    print('---')