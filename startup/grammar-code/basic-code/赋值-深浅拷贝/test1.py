# 1. 赋值：变量之间的赋值，传递的就是引用，改变其中一个变量中的内容，另外一个也会被改变
a = [1,2,3,4]
b = a
print(f"a:{a}, b:{b}, addr a:{id(a)}, addr b:{id(b)}")
# a:[1, 2, 3, 4], b:[1, 2, 3, 4], addr a:1788303039296, addr b:1788303039296
a.append(5)
print(f"a:{a}, b:{b}, addr a:{id(a)}, addr b:{id(b)}")
# a:[1, 2, 3, 4, 5], b:[1, 2, 3, 4, 5], addr a:2417535605568, addr b:2417535605568

# 2. 浅拷贝：变量内容会被重新复制一份，但是内部嵌套的内容是不会另外复制一份的
c = [1,2,3,[4,5,6]]
import copy
d = copy.copy(c)
print(f"c:{c}, d:{d}, addr c:{id(c)}, addr d:{id(d)}")
# c:[1, 2, 3, [4, 5, 6]], d:[1, 2, 3, [4, 5, 6]], addr c:2322838177472, addr d:2322838733568
print(f"c[3]:{c[3]}, d[3]:{d[3]}, addr c[3]:{id(c[3])}, addr d[3]:{id(d[3])}")
# c[3]:[4, 5, 6], d[3]:[4, 5, 6], addr c[3]:2322838178368, addr d[3]:2322838178368
c[3].append(7)
print(f"c[3]:{c[3]}, d[3]:{d[3]}, addr c[3]:{id(c[3])}, addr d[3]:{id(d[3])}")
# c[3]:[4, 5, 6, 7], d[3]:[4, 5, 6, 7], addr c[3]:2322838178368, addr d[3]:2322838178368

# 3. 深拷贝：内容都会重新复制一份
e = [1,2,3,[4,5,6]]
f = copy.deepcopy(e)

print(f"e:{e}, f:{d}, addr e:{id(e)}, addr f:{id(f)}")
# e:[1, 2, 3, [4, 5, 6]], f:[1, 2, 3, [4, 5, 6, 7]], addr e:2079276381120, addr f:2079276383744
print(f"e[3]:{e[3]}, f[3]:{f[3]}, addr e[3]:{id(e[3])}, addr f[3]:{id(f[3])}")
# e[3]:[4, 5, 6], f[3]:[4, 5, 6], addr e[3]:2079276381056, addr f[3]:2079276380992
e[3].append(7)
print(f"ec[3]:{e[3]}, f[3]:{f[3]}, addr e[3]:{id(e[3])}, addr f[3]:{id(f[3])}")
# ec[3]:[4, 5, 6, 7], f[3]:[4, 5, 6], addr e[3]:2079276381056, addr f[3]:2079276380992

# 4. 可变类型：变量对应地址的值可以修改，但是内存地址并不会发生变化
# 常见：list dict set
g = [1,2,3,4]
print(id(g))
# 2029073727872
g.append(5)
print(id(g))
# 2029073727872

f = {"name":"webster", "age":"25"}
print(f"f:{f}, addr of f:{id(f)}")
# f:{'name': 'webster', 'age': '25'}, addr of f:2164577293120
value = f.pop("name")
print(f"f:{f}, addr of f:{id(f)}")
# f:{'age': '25'}, addr of f:2164577293120

g = {1,2,3,3}
print(f"g: {g}, addr of f:{id(g)}")
# g: {1, 2, 3}, addr of f:1277319131456
g.add(6)
print(f"g: {g}, addr of f:{id(g)}")
# g: {1, 2, 3, 6}, addr of f:1277319131456

# 5. 不可变对象：变量对应的值,存储空间中保存的数据不允许修改,修改之后其实是重新生成新的内存空间存储值,地址会发生变化
# 常见: 数值类型(int bool float complex) 字符串(str) 元组(tuple)

h =10
print(f"修改前 h:{h} addr of h:{id(h)}")
# 修改前 h:10 addr of h:1723915043344

h=20
print(f"修改后 h:{h} addr of h:{id(h)}")
# 修改后 h:20 addr of h:1723915043664

i ="webster"
print(f"修改前 i:{i} addr of i:{id(i)}")
# 修改前 i:webster addr of i:1572782912048
i = "yuanwei"
print(f"修改后 i:{i} addr of i:{id(i)}")
# 修改后 i:yuanwei addr of i:1572782913328

# 所以深浅拷贝是针对可变对象的,不可变对象不存在这个说法