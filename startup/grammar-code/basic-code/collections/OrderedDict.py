from collections import OrderedDict

od = OrderedDict([('red', 1), ('blue', 2), ('green', 3)])
od.move_to_end('red')
print(od)
# OrderedDict([('blue', 2), ('green', 3), ('red', 1)])
