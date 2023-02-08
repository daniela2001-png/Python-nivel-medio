"""
Sets features in Python:
    1) Mutable / Can be modified 
    2) Not are sorted
    3) doesn't allows duplicateds
"""

set_countries = {'col', 'mex', 'arg'}
#print(set_countries)
#print(isinstance(set_countries, set))

# Sets can have many type of values, as follows:
set_many_types = {'string', 2.3, 45, True, False}
#print(set_many_types)

# also we can declare a new set as follows:
my_set = set(('abc', 'cv', 'cv', 'dani', 0))
#print(my_set)

# Now we can pass to execute some CRUD operations over a given set:
crud_set = {'daniela', 'yeinmy', 'pepito', 'andres', 'yeinmy'}

# checking the lenght of a set
size_set = len(crud_set)
print(size_set)

# checking  if an element exists in the set
print(('daniela' in crud_set) or ('ju' in crud_set))

# Now we add a new element in the set:
crud_set.add('jannin')
print(crud_set)

# update method: allows add element's **iterable**:
crud_set.update([1234, 5678])
print(crud_set)

# remove an element from the set
crud_set.remove('yeinmy')
print(crud_set)
# what happens if we try to delete again the same element with the method remove() ?
# a keyerror exception will be raised
# crud_set.remove('yeinmy')
# print(crud_set)

# instead if we can try delete a non-existent element and we want that not raise a KeyError exception we should use the discard() method, as follows:
crud_set.discard('yeinmy')
print(crud_set)

# Now if we wish delete all elements from a set we just use the clear() method, as follows:
crud_set.clear()
print(crud_set)  # will return an empty set
