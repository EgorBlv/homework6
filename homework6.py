my_dict = { 'Ivan' : 1999, 'Anton' : 2001, 'Max' : 1999}
print(my_dict)
print(my_dict ['Max'])
print(my_dict.get( 'Vlad'))
my_dict.update({'Joe' : 1997, 'Vito' : 2000})
print(my_dict)
my_dict.pop( 'Max')
print(my_dict)

my_set = {1 , 2 , 3 , 1 , 3 , 2, True, 'dark', (3, 4, 5)}
print(my_set)
my_set.add(5)
my_set.add(606)
print(my_set)
my_set.discard(3)
print(my_set)
