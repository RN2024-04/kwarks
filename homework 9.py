def print_params(a=1, b="строка", c=True):
    print(a,b,c)

print_params()
print_params(2,6)
print_params(b=25)
print_params(c=[1,2,3])

def print_params(*args, **kwargs):
    print(args,kwargs)
values_list = [1, "Анна", False]
values_dict = {"a":15, "b":"Миша", "c": True}

print_params(*values_list, **values_dict)

def print_params(*args, **kwargs):
     print(args,kwargs)
values_list_2 = [581, "LUna"]
print_params(*values_list_2, 42)

