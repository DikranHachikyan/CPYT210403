
if __name__ == '__main__':
    users = ['anna','maria','markus','florian','john', 'jane']
    mails = ['anna@no.com', 'maria@no.com','markus@no.com',
             'florian@no.com','john@no.com','']

    for data in zip(users, mails):
        name, mail = data
        print(f'user = {name} => {mail}')
        
    print('---')