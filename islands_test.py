import islands as i

g = i.Grid((4, 4), 'X', '-')

print g
print g.num_islands()


g2 = i.Grid((1, 10), 'X', '-')

print g2
print g2.num_islands()
import pdb; pdb.set_trace()
