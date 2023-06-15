set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# the union between two sets can be executed throug of two different ways:

# number one -> using the method "union" as follows:
union_of_sets = set_a.union(set_b)
print(union_of_sets)

# number two -> using the operator "|" as follows:
union_of_sets = set_a | set_b
print(union_of_sets)

# the inner join between two sets can be executed of two ways:

# number one -> using the method "intersection" as follows:
inner_sets = set_a.intersection(set_b)
print(inner_sets)

# number two -> using the operator "&" as follows:
inner_sets = set_a & set_b
print(inner_sets)

# the difference between two sets can be execute of two ways:

# number one -> using the method "difference":
difference_sets = set_a.difference(set_b)
print(difference_sets)

# number two -> usign the operator "-" :
difference_sets = set_a - set_b
print(difference_sets)
difference_sets = set_b - set_a
print(difference_sets)

# the symmetric difference between two sets is equal to union of them minus their intersection

# number one -> doing first an union method minus their intersection
symmetric_dif = (set_a.union(set_b) - (set_a & set_b))
print(symmetric_dif)

# number two -> using the operator "^":
symmetric_dif = set_a ^ set_b
print(symmetric_dif)
