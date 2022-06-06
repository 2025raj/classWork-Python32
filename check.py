
# creating a empty dictionary
'''
dict_var = {}
check = isinstance(dict_var, dict)
print(check)
'''

# checking:
'''
dict_var = {1, 2, 3}
check = isinstance(dict_var, dict)
print(check)
'''
'''
# keys must be unique but it's ok to have (same keyword) with different values no error but we lose data @garbage collection occurs..
# dictionary : allows multiple data-types. 
 
dict_var = {"name": "raj", "age": 3, "height": 5.7,
            1: "babu", 1.5: "hero", "a": "changed result"}   
check = isinstance(dict_var, dict)
print(check)


print(dict_var)

'''

'''
direct_var = {"name": "raj", "age": 20}
key_val = direct_var["name"]
print(key_val)

'''

'''
a = {}
print(type(a))

b = set()
print(type(b))

c = ()
print(type(c))

d = []
print(type(d))
'''

'''
a = int(input("enter a num to find it's factorial: "))
i = 1
fact = 1
while i <= a:
    fact = fact * i
    i = i + 1
print(f"the {a}! is : {fact}")

'''
'''
Ascen_odr = [18, 1, 55, 2, 30]
# print(Ascen_odr)
num = Ascen_odr.sort(reverse=False)
print(num)

'''
