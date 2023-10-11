# lists use *[]* and tuples use *()*

empty_tuple = ()

# the comma indicates tuple rather than ordinary single value
one_element_tup_a = (1, )
one_element_tup_b = 1,

# when more than one value in tuple, final comma (and paretheses) are optional
three_element_tup = 1, 2, 3
print(three_element_tup)

''' 
mutability: lists are mutable (add/delete/swap easily);  

no modifying with tuples (immutable)
E.g., 
!X: *del user_data[0]*; 
!X: *.append('item')); 
!X: no indexing to change indiv. elements (indexing to read: OK)

strings are also immutable (can access individual characters, but not replace them)
like tuples, must replace entire string
'''