from Polynomial import Polynomial

poly = Polynomial(3, "x")
poly.generate_equation_sequential(2, 1, 2)
print(poly.get_equation())

list = poly.get_variable_list()
for index in range(len(list)):
    print(list[index].get_function())