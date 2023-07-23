from matrix import Matrix
a = Matrix([[2,2], [1,2]])
b = Matrix([[2,2], [1,2]])
c = a - b
print(c)
c = a + b
print(c)
c = a * b
print(c)
c = a * 2
print(c)
d = Matrix([[1,2,3],[3,4,5]])
e = Matrix([[1,2,3],[4,5,6]])
f = d.transpose()
g = e @ f #'2x3, 3x2'
print(f)
print(g)