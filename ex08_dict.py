# %%
connection = dict(
    host='localhost', 
    db='northwind', 
    is_admin=True,
    port=3306 
)

connection
# %%
connection['port']
# %%
connection1 = ['localhost', 3306, 'northwind', True]
# %%
user = {
    'first_name':'Anna',
    'last_name':'Smith',
    'age':30,
    'email':'anna@no.com'
}

user['first_name']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
user['phone']
# %%
'phone' in user
# %%
user.get('phone','000-00-00')
# %%
