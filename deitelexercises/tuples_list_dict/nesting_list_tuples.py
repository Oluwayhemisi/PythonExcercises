animals = ["lion","tiger", "frumious"]
large_cats = animals
large_cats.append("leopard")
print(large_cats)

large_cats = animals[:]
large_cats.append("fox")
print(large_cats)

matrix1 = [[1,2],[3,4]]
matrix2 = matrix1[:]
matrix2[0] = [5,6]
print(matrix2)
