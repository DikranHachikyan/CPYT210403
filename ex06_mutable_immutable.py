# %%
a = 5
b = 5

id(a) == id(b)
# %%
a = 5

print(id(a))

a = 10
print(id(a))
# %%
class Point:
    def __init__(self, x):
        self.x = x

# %%
p1 = Point(x = 10)
p2 = Point(x = 10)

id(p1) == id(p2)

# %%
id(p1)
# %%
p1.x = 10
id(p1)
# %%
id(p1.x) == id(p2.x)
# %%

s1 = 'hello' * 1000
s2 = 'hello' * 1000

id(s1) == id(s2)
# %%
